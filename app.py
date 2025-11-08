import streamlit as st

# --- Hàm API Logic (Được bao bọc lại từ Bước 2) ---
def generate_prompt_wrapper(image_input, update_command_input):
    
    if image_input is None:
        return "⚠️ Lỗi: Vui lòng tải lên một hình ảnh để bắt đầu Phân tích Prompt (Bước 1)."
    
    # Logic kiểm tra cú pháp và logic phân tích hình ảnh (giả lập)
    if update_command_input:
        if "Cập nhật ghi nhớ:" not in update_command_input:
            return "⚠️ Sai cú pháp: Lệnh cập nhật phải bắt đầu bằng 'Cập nhật ghi nhớ:'"
    
    # Giả lập kết quả phân tích thành công
    memory_store = {
        'chu_the': "A striking male portrait, wearing an all-black minimalist suit, slicked-back dark hair, pensive expression.",
        'boi_canh': "Shot in a light neutral grey studio against a plain backdrop, with strong, controlled artificial light from the top-right.",
        'ky_thuat': "4:5 Vertical Portrait, Medium Close-up, 50mm Prime Lens, Very Shallow Depth of Field (f/1.4)."
    }
    
    # Tổng hợp và Định dạng Prompt cuối cùng theo Bước 3
    final_prompt = (
        f"Detailed Descriptive Prompt: {memory_store['chu_the']}, {memory_store['boi_canh']}, "
        f"captured using a {memory_store['ky_thuat'].split(', ')[2]}, {memory_store['ky_thuat'].split(', ')[3]}, "
        f"with a {memory_store['ky_thuat'].split(', ')[4].replace(' (f/1.4)', '')} --ar 4:5"
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
    # Đầu vào Hình ảnh Streamlit
    image_file = st.file_uploader("Tải Lên Hình Ảnh Chân Dung (Bước 1)", type=['png', 'jpg', 'jpeg'])
    
with col2:
    # Đầu ra Prompt Streamlit
    prompt_output = st.empty()

# Đầu vào Tùy chọn Cập nhật (Bước 4)
update_input = st.text_area(
    "Điều Chỉnh/Cập Nhật Ghi Nhớ (Tùy Chọn - Bước 4)",
    placeholder="Ví dụ: Cập nhật ghi nhớ: [câu hỏi thứ (1):(Màu sắc trang phục là Deep Forest Green)]"
)

# Nút Kích hoạt
if st.button("✨ TẠO PROMPT TỐI ƯU ✨"):
    if image_file is not None:
        # Giả sử ảnh đã được tải lên và xử lý
        result = generate_prompt_wrapper("file_uploaded", update_input) # "file_uploaded" là placeholder cho path/data
        prompt_output.text_area("▶️ Detailed Descriptive Prompt (Kết Quả)", result, height=200)
    else:
        prompt_output.text_area("▶️ Detailed Descriptive Prompt (Kết Quả)", "⚠️ Vui lòng tải lên một hình ảnh!", height=200)