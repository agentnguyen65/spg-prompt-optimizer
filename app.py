import streamlit as st

# --- Hàm API Logic (Được bao bọc lại từ Bước 2) ---
def generate_prompt_wrapper(image_input, update_command_input):
    
    # KHI KHÔNG CÓ HÌNH ẢNH, DỮ LIỆU SẼ KHÔNG ĐƯỢC PHÂN TÍCH ĐẦY ĐỦ
    if image_input == "placeholder_no_file":
        return "⚠️ Lỗi: Vui lòng tải lên một hình ảnh để bắt đầu Phân tích Prompt (Bước 1)."
    
    # Logic kiểm tra cú pháp (Giữ nguyên)
    if update_command_input:
        if "Cập nhật ghi nhớ:" not in update_command_input:
            return "⚠️ Sai cú pháp: Lệnh cập nhật phải bắt đầu bằng 'Cập nhật ghi nhớ:'"
    
    # Giả lập kết quả phân tích thành công (Dữ liệu phải đảm bảo có 5 phần tử trở lên)
    # LƯU Ý: Đảm bảo có đủ 5 phần tử (index 0 đến 4) 
    memory_store = {
        'chu_the': "A striking male portrait, wearing an all-black minimalist suit, slicked-back dark hair, pensive expression.",
        'boi_canh': "Shot in a light neutral grey studio against a plain backdrop, with strong, controlled artificial light from the top-right.",
        'ky_thuat': "4:5 Vertical Portrait, Medium Close-up, 50mm Prime Lens, Very Shallow Depth of Field (f/1.4), Detailed Lighting Analysis" 
        # Đã thêm phần tử thứ 5 (index 4) để tránh lỗi Index 
    }
    
    # Chắc chắn rằng mảng có đủ phần tử trước khi truy cập index [2], [3], [4]
    ky_thuat_parts = memory_store['ky_thuat'].split(', ')
    if len(ky_thuat_parts) < 5:
        return "⚠️ Lỗi Giả Lập Dữ Liệu: Dữ liệu 'ky_thuat' không đủ 5 phần tử để tạo Prompt chi tiết."

    # Tổng hợp và Định dạng Prompt cuối cùng
    final_prompt = (
        f"Detailed Descriptive Prompt: {memory_store['chu_the']}, {memory_store['boi_canh']}, "
        f"captured using a {ky_thuat_parts[2]}, {ky_thuat_parts[3]}, "
        f"with a {ky_thuat_parts[4].replace(' (f/1.4)', '').replace('(f/1.4)', '')} --ar 4:5"
    )
    
    return final_prompt
# --------------------------------------------------

# Xây dựng giao diện Streamlit
st.set_page_config(page_title="SPG-WebApp: Tối Ưu Hóa Prompt Tự Động", layout="wide")

st.title("📸 Tối Ưu Hóa Prompt Tự Động (Streamlit WebApp)")
st.markdown(
    "Sử dụng công cụ này để phân tích hình ảnh và tạo Prompt siêu chi tiết dưới góc nhìn **Chuyên gia Chụp Chân dung**."
)

col1, col2 = st.columns(2)

with col1:
    image_file = st.file_uploader("Tải Lên Hình Ảnh Chân Dung (Bước 1)", type=['png', 'jpg', 'jpeg'])
    
with col2:
    prompt_output = st.empty()

update_input = st.text_area(
    "Điều Chỉnh/Cập Nhật Ghi Nhớ (Tùy Chọn - Bước 4)",
    placeholder="Ví dụ: Cập nhật ghi nhớ: [câu hỏi thứ (1):(Màu sắc trang phục là Deep Forest Green)]"
)

if st.button("✨ TẠO PROMPT TỐI ƯU ✨"):
    # Xác định giá trị cho image_input: nếu có file, dùng placeholder "file_uploaded"; nếu không, dùng "placeholder_no_file"
    input_value = "file_uploaded" if image_file is not None else "placeholder_no_file"
    
    result = generate_prompt_wrapper(input_value, update_input) 
    prompt_output.text_area("▶️ Detailed Descriptive Prompt (Kết Quả)", result, height=200)
