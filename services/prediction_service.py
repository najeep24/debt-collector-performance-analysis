import pandas as pd
import numpy as np
import dill as pickle
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.figure import Figure
import matplotlib
import shap
import lightgbm
from lightgbm import LGBMClassifier
matplotlib.use('Agg')


# Tambahkan import untuk semua transformer yang digunakan dalam model
from transformers.feature_transformer import (
    ProblemSolvingTransformer, 
    FeedbackTransformer,
    RPCTransformer,
    CEITransformer,
    PTPTransformer,
    ZScoreTransformer,
    DataTypeTransformer
)

class PredictionService:
    def __init__(self, model_path='saved_pipeline.pkl'):
        # Load the prediction model
        with open(model_path, 'rb') as file:
            self.pipeline = pickle.load(file)
            
        # Define thresholds for metrics
        self.rpc_thresholds = [0, 27, 54]
        self.ptp_thresholds = [0, 40, 80]
        self.recovery_thresholds = [0, 40, 80]
        
        # Average stats for comparison in radar chart
        self.average_stats = [87.497928, 18.750000, 75]  # RPC, PTP, Recovery Rate
    
    def preprocess_data(self, form_data):
        """Convert form data to DataFrame and perform feature engineering"""
        # Get form data
        total_debt = float(form_data['total_debt'])
        total_debt_payment_recieved = float(form_data['total_debt_payment_recieved'])
        problem_solving = form_data['problem_solving']
        transfer_day_diff = float(form_data['transfer_day_diff'])
        debtor_feedback = form_data['debtor_feedback']
        total_contact = float(form_data['total_contact'])
        contact_connected = float(form_data['contact_connected'])
        call_to_ptp = float(form_data['call_to_ptp'])
        total_case_closed = float(form_data['total_case_closed'])

        # Create DataFrame
        data = np.array([[total_debt, total_debt_payment_recieved, problem_solving,
                           transfer_day_diff, debtor_feedback, total_contact, contact_connected,
                           call_to_ptp, total_case_closed]])
        columns = ["total_debt", "total_debt_payment_recieved", "problem_solving",
                    "transfer_day_diff", "debtor_feedback", "total_contact", "contact_connected", 
                    "call_to_ptp", "total_case_closed"]
        df = pd.DataFrame(data, columns=columns)

        # Ensure numeric conversion for numeric columns
        df = df.astype({
            'total_debt': float,
            'total_debt_payment_recieved': float,
            'transfer_day_diff': float,
            'total_contact': float,
            'contact_connected': float,
            'call_to_ptp': float,
            'total_case_closed': float
        })

        # Feature Engineering
        df['RPC_rate'] = (df['contact_connected'] / df['total_contact']) * 100 if df['total_contact'].values[0] > 0 else 0
        df['PTP_rate'] = (df['call_to_ptp'] / df['contact_connected']) * 100 if df['contact_connected'].values[0] > 0 else 0
        df['recovery_rate'] = (df['total_debt_payment_recieved'] / df['total_debt']) * 100 if df['total_debt'].values[0] > 0 else 0
        
        return df
    
    def predict(self, df):
        prediction = self.pipeline.predict(df)
        return prediction
    
    def get_metric_descriptions(self, ptp, rpc, recovery_rate):
        """Generate descriptions for metrics based on thresholds"""
        descriptions = {}
        
        # PTP description
        if ptp < 50:
            descriptions['ptp'] = "Skor %PTP Anda berada di kuartil pertama, yang berarti performa Anda dalam mendapatkan janji pembayaran berada di bawah rata-rata debt collector lainnya. Untuk meningkatkan skor ini, coba evaluasi ulang pendekatan Anda dalam berkomunikasi dengan debitur dan fokus pada strategi yang dapat meningkatkan kepercayaan dan komitmen mereka untuk membayar."
        elif 50 < ptp <= 70:
            descriptions['ptp'] = "Skor %PTP Anda berada di kuartil kedua, yang berarti performa Anda berada di sekitar rata-rata debt collector. Dengan sedikit perbaikan pada strategi komunikasi dan penagihan, Anda bisa mencapai hasil yang lebih tinggi."
        else:
            descriptions['ptp'] = "Selamat! Skor %PTP Anda berada di atas 75% debt collector dalam dataset kami, menunjukkan performa yang sangat baik dalam mendapatkan janji pembayaran dari debitur."

        # RPC description
        if rpc <= 27:
            descriptions['rpc'] = "Kamu perlu fokus untuk meningkatkan jumlah panggilan yang berhasil tersambung. Cobalah mengatur ulang waktu panggilanmu agar lebih strategis, seperti menelepon pada jam-jam sibuk debitur atau saat mereka lebih mungkin merespons. Pastikan informasi kontak yang kamu gunakan sudah benar dan selalu cek kembali sebelum menelepon. Jangan lupa untuk lebih percaya diri dalam berbicara dan sampaikan tujuanmu dengan jelas"
        elif 27 < rpc <= 54:
            descriptions['rpc'] = "Kamu sudah cukup baik dalam menghubungi debitur, tetapi masih ada ruang untuk meningkatkan efektivitas. Cobalah gunakan pendekatan yang lebih persuasif dalam komunikasi dan pastikan setiap percakapan meninggalkan kesan yang baik. Skrip panggilan yang jelas dapat sangat membantu, tetapi jangan lupa untuk menambahkan sentuhan personal agar debitur merasa lebih nyaman"
        else:
            descriptions['rpc'] = "Kerja kerasmu dalam memastikan panggilan tersambung sangat luar biasa! Pertahankan pencapaian ini, dan kalau bisa, ajarkan rekan-rekanmu cara kamu melakukannya. Kamu juga bisa mulai mencoba menangani kasus yang lebih sulit untuk meningkatkan pengalamanmu. Teruslah mempertahankan semangat ini!"

        # Recovery rate description
        if recovery_rate <= 40:
            descriptions['recovery'] = "Skor Success Ratio Anda berada di kuartil pertama, menunjukkan bahwa performa Anda dalam menutup kasus berada di bawah rata-rata debt collector lainnya. Disarankan untuk meninjau ulang pendekatan Anda dalam menangani kasus dan mencari cara untuk menyelesaikan lebih banyak kasus secara efektif. Mungkin Anda perlu memperkuat tim Anda atau memperbaiki proses internal untuk mencapai hasil yang lebih baik."
        elif 40 < recovery_rate <= 80:
            descriptions['recovery'] = "Skor Success Ratio Anda berada di kuartil kedua, yang berarti performa Anda dalam menutup kasus berada di sekitar rata-rata. Dengan beberapa penyesuaian pada strategi dan proses, Anda bisa meningkatkan rasio keberhasilan Anda."
        else:
            descriptions['recovery'] = "Selamat! Skor Success Ratio Anda berada di atas 75% debt collector dalam dataset kami, menunjukkan performa yang sangat baik dalam menutup kasus."
            
        return descriptions
    
    
    
    def generate_charts(self, rpc, ptp, recovery_rate, shap_values=None, df=None):
        """Generate visualization charts for the metrics"""
        chart_data = {}
        
        # Labels for radar chart
        labels = ['RPC rate', 'PTP rate', 'Recovery_rate']
        stats = [rpc, ptp, recovery_rate]
        
        # Radar chart
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        stats_closed = stats + stats[:1]  # Close the polygon
        angles_closed = angles + angles[:1]  # Close the angles
        average_stats_closed = self.average_stats + self.average_stats[:1]  # Close the average stats
        
        ax.fill(angles_closed, stats_closed, color='blue', alpha=0.25, label='Collector Score')
        ax.plot(angles_closed, stats_closed, color='blue', linewidth=2)
        
        ax.fill(angles_closed, average_stats_closed, color='gray', alpha=0.15, label='Average Score')
        ax.plot(angles_closed, average_stats_closed, color='gray', linewidth=2, linestyle='dashed')
        
        ax.set_yticklabels([])
        ax.set_xticks(angles)
        ax.set_xticklabels(labels)
        ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
        
        # Save radar chart to base64
        radar_img = io.BytesIO()
        fig.savefig(radar_img, format='png')
        radar_img.seek(0)
        chart_data['radar'] = base64.b64encode(radar_img.getvalue()).decode()
        
        # RPC gauge chart
        fig2, ax2 = plt.subplots(figsize=(3.8, 2))
        ax2.barh([''], rpc, color='blue', align='center')
        for threshold in self.rpc_thresholds:
            ax2.axvline(threshold, color=['red', 'orange', 'green'][self.rpc_thresholds.index(threshold)], linewidth=2)
        ax2.set_xlim(0, 100)
        ax2.set_xlabel('RPC Ratio')
        
        # Save RPC chart to base64
        rpc_img = io.BytesIO()
        fig2.savefig(rpc_img, format='png')
        rpc_img.seek(0)
        chart_data['rpc'] = base64.b64encode(rpc_img.getvalue()).decode()
        
        # PTP gauge chart
        fig3, ax3 = plt.subplots(figsize=(3.8, 2))
        ax3.barh([''], ptp, color='green', align='center')
        for threshold in self.ptp_thresholds:
            ax3.axvline(threshold, color=['red', 'orange', 'green'][self.ptp_thresholds.index(threshold)], linewidth=2)
        ax3.set_xlim(0, 57)
        ax3.set_xlabel('PTP Ratio')
        
        # Save PTP chart to base64
        ptp_img = io.BytesIO()
        fig3.savefig(ptp_img, format='png')
        ptp_img.seek(0)
        chart_data['ptp'] = base64.b64encode(ptp_img.getvalue()).decode()
        
        # Recovery rate gauge chart
        fig4, ax4 = plt.subplots(figsize=(3.8, 2))
        ax4.barh([''], recovery_rate, color='orange', align='center')
        for threshold in self.recovery_thresholds:
            ax4.axvline(threshold, color=['red', 'orange', 'green'][self.recovery_thresholds.index(threshold)], linewidth=2)
        ax4.set_xlim(0, 100)
        ax4.set_xlabel('Recovery ratio')
        
        # Save recovery rate chart to base64
        recovery_img = io.BytesIO()
        fig4.savefig(recovery_img, format='png')
        recovery_img.seek(0)
        chart_data['recovery'] = base64.b64encode(recovery_img.getvalue()).decode()
        
        return chart_data