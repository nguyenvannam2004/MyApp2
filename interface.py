import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Tải mô hình đã huấn luyện
model = joblib.load("C:/Users/Nam's computer/Desktop/python/logistic_model.pkl")

# Hàm dự đoán bệnh tim
def predict_heart_disease():
    try:
        # Lấy dữ liệu từ giao diện
        age = float(entry_age.get())
        sex = float(entry_sex.get())
        cp = float(entry_cp.get())
        trestbps = float(entry_trestbps.get())
        chol = float(entry_chol.get())
        fbs = float(entry_fbs.get())
        restecg = float(entry_restecg.get())
        thalach = float(entry_thalach.get())
        exang = float(entry_exang.get())
        oldpeak = float(entry_oldpeak.get())
        slope = float(entry_slope.get())
        ca = float(entry_ca.get())
        thal = float(entry_thal.get())

        # Tạo mảng dữ liệu đưa vào mô hình (phải phù hợp với cấu trúc mô hình đã huấn luyện)
        new_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Dự đoán với mô hình đã huấn luyện
        prediction = model.predict(new_data)

        # Hiển thị kết quả dự đoán
        if prediction[0] == 1:
            messagebox.showinfo("Kết quả", "Bệnh nhân này có nguy cơ bị bệnh tim.")
        else:
            messagebox.showinfo("Kết quả", "Bệnh nhân này không có nguy cơ bị bệnh tim.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập dữ liệu hợp lệ.")

# Tạo giao diện
root = tk.Tk()
root.title("Dự đoán Bệnh Tim")

# Nhãn và ô nhập liệu cho các yếu tố đầu vào
label_age = tk.Label(root, text="Tuổi:")
label_age.grid(row=0, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=0, column=1)

label_sex = tk.Label(root, text="Giới tính (0: Nữ, 1: Nam):")
label_sex.grid(row=1, column=0)
entry_sex = tk.Entry(root)
entry_sex.grid(row=1, column=1)

label_cp = tk.Label(root, text="Loại đau ngực (0-3):")
label_cp.grid(row=2, column=0)
entry_cp = tk.Entry(root)
entry_cp.grid(row=2, column=1)

label_trestbps = tk.Label(root, text="Huyết áp khi nghỉ (mm Hg):")
label_trestbps.grid(row=3, column=0)
entry_trestbps = tk.Entry(root)
entry_trestbps.grid(row=3, column=1)

label_chol = tk.Label(root, text="Cholesterol (mg/dl):")
label_chol.grid(row=4, column=0)
entry_chol = tk.Entry(root)
entry_chol.grid(row=4, column=1)

label_fbs = tk.Label(root, text="Đường huyết lúc đói (> 120 mg/dl, 1: có, 0: không):")
label_fbs.grid(row=5, column=0)
entry_fbs = tk.Entry(root)
entry_fbs.grid(row=5, column=1)

label_restecg = tk.Label(root, text="Kết quả điện tâm đồ (0, 1, 2):")
label_restecg.grid(row=6, column=0)
entry_restecg = tk.Entry(root)
entry_restecg.grid(row=6, column=1)

label_thalach = tk.Label(root, text="Nhịp tim tối đa:")
label_thalach.grid(row=7, column=0)
entry_thalach = tk.Entry(root)
entry_thalach.grid(row=7, column=1)

label_exang = tk.Label(root, text="Có đau thắt ngực khi gắng sức không (1: có, 0: không):")
label_exang.grid(row=8, column=0)
entry_exang = tk.Entry(root)
entry_exang.grid(row=8, column=1)

label_oldpeak = tk.Label(root, text="ST depression induced by exercise:")
label_oldpeak.grid(row=9, column=0)
entry_oldpeak = tk.Entry(root)
entry_oldpeak.grid(row=9, column=1)

label_slope = tk.Label(root, text="Slope của ST segment (0-2):")
label_slope.grid(row=10, column=0)
entry_slope = tk.Entry(root)
entry_slope.grid(row=10, column=1)

label_ca = tk.Label(root, text="Số lượng mạch máu chính (0-3):")
label_ca.grid(row=11, column=0)
entry_ca = tk.Entry(root)
entry_ca.grid(row=11, column=1)

label_thal = tk.Label(root, text="Thalassemia (0: không, 1: bình thường, 2: khiếm khuyết, 3: nghiêm trọng):")
label_thal.grid(row=12, column=0)
entry_thal = tk.Entry(root)
entry_thal.grid(row=12, column=1)

# Nút "Dự đoán"
btn_predict = tk.Button(root, text="Dự đoán", command=predict_heart_disease)
btn_predict.grid(row=13, column=0, columnspan=2)

# Chạy giao diện
root.mainloop()
