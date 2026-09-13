# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Minh Tuấn  
> **Mã Sinh Viên / Mã Học viên:** 2A202602850  
> **Chủ đề Lựa chọn:** Trợ lý Tuyển dụng & Sàng lọc CV: Tra cứu tiêu chí tuyển dụng vị trí và gửi thông báo lịch phỏng vấn.

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5/ 5 | Bài toán cần chia nhỏ ra các bước multistep như sau : Nhận diện yêu cầu vị trí tuyển dụng và phân tích cv -> tra cứu tiêu chí tuyển dụng trên hệ thống tương ứng -> so khớp hồ sơ với các tiêu chí của từng yêu cầu tuyển dụng trên hệ thống để ra kết luận ( pass/not pass) -> lên nội dung và kích hoạt gửi lịch hẹn phỏng vấn phù hợp |
| **2. Tool Interaction** | 3/ 5 | có cần kết nối ra bên ngoài vì yêu cầu tuyển dụng có thể có mới hàng ngày và thay đổi linh động.Ví dụ :Tool 1 : tra cứu csdl tiêu chí vị trí tuyển dụng hoặc hồ sơ ứng viên , tool 2 : gửi thông báo lịch phỏng vấn tới ứng viên và lưu vào mail của công ty  |
| **3. Dynamic Decision** | 4/ 5 | Có kết quả phần trước nếu pass thì hệ thống sẽ gửi lịch còn nếu không pass thì soạn thư từ chối|
| **4. Long Horizon Goal** | 4 / 5 | Có vì nếu ứng viên phản hồi về việc lịch chưa phù hợp phải get được lịch sử để xem đã thảo luận ngày nào hay thiếu gì để bổ sung và thay thế gửi tới ứng viên |
| **TỔNG ĐIỂM AGENTIC FIT** | 16/ 20 | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Chào bạn, bạn có thể giới thiệu quy trình tuyển dụng và các vòng phỏng vấn cơ bản của công ty không?",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Chào bạn! Rất vui được chia sẻ với bạn về quy trình tuyển dụng tiêu chuẩn và các vòng phỏng vấn cơ bản tại công ty chúng tôi. Quy trình này được thiết kế nhằm đảm bảo tính khách quan, hiệu quả và giúp cả hai bên (công ty và ứng viên) có cơ hội tìm hiểu nhau một cách tốt nhất.\n\nThông thường, quy trình tuyển dụng sẽ trải qua **5 bước cơ bản** sau:\n\n### 1. Vòng 1: Tiếp nhận & Sàng lọc Hồ sơ (CV Screening)\n*   **Mục tiêu:** Bộ phận Tuyển dụng (HR) sẽ xem xét CV của bạn để đánh giá mức độ phù hợp ban đầu về học vấn, kinh nghiệm làm việc, kỹ năng chuyên môn và các dự án đã thực hiện so với yêu cầu của vị trí tuyển dụng.\n*   **Thời gian phản hồi:** Thường từ 3 - 7 ngày làm việc kể từ khi nhận được hồ sơ.\n\n### 2. Vòng 2: Phỏng vấn Sơ loại (HR Screening Interview)\n*   **Hình thức:** Gọi điện thoại (Phone Screen) hoặc phỏng vấn trực tuyến (Online qua Zoom/Teams) khoảng 15 - 30 phút.\n*   **Người thực hiện:** Chuyên viên Tuyển dụng (HR Recruiter).\n*   **Nội dung:** \n    *   Xác nhận lại các thông tin trong CV.\n    *   Tìm hiểu về định hướng nghề nghiệp, mong muốn thu nhập, thời gian có thể bắt đầu công việc.\n    *   Đánh giá sơ bộ về kỹ năng giao tiếp, thái độ và mức độ phù hợp với văn hóa công ty.\n\n### 3. Vòng 3: Đánh giá Năng lực / Bài Test Chuyên Môn (tùy vị trí)\n*   **Hình thức:** Làm bài test online, bài tập tình huống (Case study) hoặc bài thực hành kỹ thuật (Coding test, Design test,...).\n*   **Mục tiêu:** Đánh giá tư duy logic, kỹ năng giải quyết vấn đề và năng lực chuyên môn thực tế của bạn trước khi bước vào vòng phỏng vấn sâu.\n\n### 4. Vòng 4: Phỏng vấn Chuyên môn & Kỹ thuật (Technical/Professional Interview)\n*   **Hình thức:** Phỏng vấn trực tiếp tại văn phòng hoặc trực tuyến (từ 45 - 90 phút).\n*   **Người thực hiện:** Trưởng bộ phận chuyên môn (Line Manager) và các thành viên chủ chốt trong đội ngũ (Key Members).\n*   **Nội dung:**\n    *   Đi sâu vào các dự án, kinh nghiệm thực tế bạn đã làm.\n    *   Giải quyết các bài toán/tình huống giả định liên quan trực tiếp đến công việc hàng ngày.\n    *   Đánh giá sâu về tư duy chuyên môn, khả năng làm việc nhóm và khả năng chịu áp lực.\n\n### 5. Vòng 5: Phỏng vấn Chung cuộc (Final Interview - nếu có)\n*   **Người thực hiện:** Giám đốc bộ phận (Director) hoặc Ban Giám đốc (C-level).\n*   **Nội dung:** Trao đổi về tầm nhìn, định hướng phát triển dài hạn của bạn tại công ty, cũng như thống nhất về các chế độ đãi ngộ và kỳ vọng từ cả hai phía.\n\n### 6. Tiếp nhận Thư mời nhận việc (Offer Letter)\n*   Nếu bạn vượt qua các vòng trên, HR sẽ liên hệ để trao đổi chi tiết về mức lương, thưởng, chế độ phúc lợi và gửi Thư mời nhận việc chính thức (Offer Letter) qua email.\n\n---\n*Lưu ý: Quy trình trên có thể được điều chỉnh linh hoạt (rút gọn hoặc thêm bước) tùy thuộc vào cấp bậc và đặc thù của từng vị trí tuyển dụng.*\n\nNếu bạn đang quan tâm đến một vị trí cụ thể hoặc muốn tra cứu trạng thái hồ sơ của mình, hãy cung cấp mã ứng viên hoặc thông tin vị trí để tôi hỗ trợ bạn chi tiết hơn nhé!",
    "latency_ms": 6651.23
  },
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin hồ sơ và kết quả sàng lọc CV của ứng viên UV2026001.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "candidate_query",
    "arguments": {
      "candidate_id": "UV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "candidate_id": "UV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "applied_role": "Kỹ sư AI / Machine Learning",
        "experience_years": 3,
        "skills": [
          "Python",
          "PyTorch",
          "LLM",
          "MCP"
        ],
        "email": "an.nguyen@example.com",
        "screening_status": "ĐẠT - Đủ điều kiện phỏng vấn chuyên môn",
        "assigned_interviewer": "Trưởng phòng Kỹ thuật"
      }
    },
    "latency_ms": 1615.48
  },
  {
    "step": 2,
    "query": "Hãy tra cứu thông tin hồ sơ và kết quả sàng lọc CV của ứng viên UV2026001.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Hồ sơ ứng viên UV2026001 (Nguyễn Văn An): Vị trí ứng tuyển: Kỹ sư AI / Machine Learning, Kinh nghiệm: 3 năm, Kỹ năng: Python, PyTorch, LLM, MCP, Trạng thái sàng lọc: ĐẠT - Đủ điều kiện phỏng vấn chuyên môn, Người phụ trách phỏng vấn: Trưởng phòng Kỹ thuật.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Ứng viên UV2026001 đã đạt vòng duyệt hồ sơ. Hãy đặt lịch phỏng vấn vòng 1 cho ứng viên này vào lúc 14:00 ngày 20/09/2026 với người phỏng vấn là Trưởng phòng Tuyển dụng.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_interview",
    "arguments": {
      "datetime_str": "14:00 20/09/2026",
      "candidate_id": "UV2026001",
      "interviewer": "Trưởng phòng Tuyển dụng",
      "round": "Vòng 1"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "INT-UV2026001-2026",
      "candidate_id": "UV2026001",
      "datetime": "14:00 20/09/2026",
      "interviewer": "Trưởng phòng Tuyển dụng",
      "round": "Vòng 1",
      "message": "Đã đặt lịch phỏng vấn thành công cho ứng viên UV2026001 vào lúc 14:00 20/09/2026 với Trưởng phòng Tuyển dụng (Vòng 1). Thông báo đã được gửi đến ứng viên."
    },
    "latency_ms": 2326.42
  },
  {
    "step": 2,
    "query": "Ứng viên UV2026001 đã đạt vòng duyệt hồ sơ. Hãy đặt lịch phỏng vấn vòng 1 cho ứng viên này vào lúc 14:00 ngày 20/09/2026 với người phỏng vấn là Trưởng phòng Tuyển dụng.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đã đặt lịch phỏng vấn thành công cho ứng viên UV2026001 vào lúc 14:00 20/09/2026 với Trưởng phòng Tuyển dụng (Vòng 1). Thông báo đã được gửi đến ứng viên.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Hãy kiểm tra thông tin hồ sơ của ứng viên UV2026001 xem người phụ trách phỏng vấn chuyên môn là ai, sau đó đặt lịch phỏng vấn với người đó vào lúc 09:30 ngày 22/09/2026 giúp tôi.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "candidate_query",
    "arguments": {
      "candidate_id": "UV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "candidate_id": "UV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "applied_role": "Kỹ sư AI / Machine Learning",
        "experience_years": 3,
        "skills": [
          "Python",
          "PyTorch",
          "LLM",
          "MCP"
        ],
        "email": "an.nguyen@example.com",
        "screening_status": "ĐẠT - Đủ điều kiện phỏng vấn chuyên môn",
        "assigned_interviewer": "Trưởng phòng Kỹ thuật"
      }
    },
    "latency_ms": 2037.76
  },
  {
    "step": 2,
    "query": "Hãy kiểm tra thông tin hồ sơ của ứng viên UV2026001 xem người phụ trách phỏng vấn chuyên môn là ai, sau đó đặt lịch phỏng vấn với người đó vào lúc 09:30 ngày 22/09/2026 giúp tôi.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_interview",
    "arguments": {
      "round": "Phỏng vấn chuyên môn",
      "interviewer": "Trưởng phòng Kỹ thuật",
      "candidate_id": "UV2026001",
      "datetime_str": "09:30 22/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "INT-UV2026001-2026",
      "candidate_id": "UV2026001",
      "datetime": "09:30 22/09/2026",
      "interviewer": "Trưởng phòng Kỹ thuật",
      "round": "Phỏng vấn chuyên môn",
      "message": "Đã đặt lịch phỏng vấn thành công cho ứng viên UV2026001 vào lúc 09:30 22/09/2026 với Trưởng phòng Kỹ thuật (Phỏng vấn chuyên môn). Thông báo đã được gửi đến ứng viên."
    },
    "latency_ms": 4388.66
  },
  {
    "step": 3,
    "query": "Hãy kiểm tra thông tin hồ sơ của ứng viên UV2026001 xem người phụ trách phỏng vấn chuyên môn là ai, sau đó đặt lịch phỏng vấn với người đó vào lúc 09:30 ngày 22/09/2026 giúp tôi.",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Dựa trên thông tin tra cứu và kết quả thực hiện từ hệ thống, tôi xin gửi đến bạn báo cáo chi tiết như sau:\n\n1. **Thông tin ứng viên & Người phụ trách phỏng vấn:**\n   * **Ứng viên:** Nguyễn Văn An (Mã định danh: `UV2026001`)\n   * **Vị trí ứng tuyển:** Kỹ sư AI / Machine Learning\n   * **Người phụ trách phỏng vấn chuyên môn:** **Trưởng phòng Kỹ thuật**\n\n2. **Kết quả đặt lịch phỏng vấn:**\n   * **Thời gian:** 09:30 ngày 22/09/2026\n   * **Người phỏng vấn:** Trưởng phòng Kỹ thuật\n   * **Vòng phỏng vấn:** Phỏng vấn chuyên môn\n   * **Mã lịch hẹn (Booking ID):** `INT-UV2026001-2026`\n   * **Trạng thái:** **Thành công**. Hệ thống đã tự động gửi thông báo lịch hẹn chi tiết đến email của ứng viên Nguyễn Văn An (`an.nguyen@example.com`).",
    "latency_ms": 4616.61
  },
  {
    "step": 1,
    "query": "Hãy tra cứu hồ sơ và trạng thái sàng lọc CV của ứng viên có mã UV9999999.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "candidate_query",
    "arguments": {
      "candidate_id": "UV9999999"
    },
    "observation": {
      "status": "NOT_FOUND",
      "message": "Không tìm thấy dữ liệu hồ sơ ứng viên có mã 'UV9999999'"
    },
    "latency_ms": 1622.89
  },
  {
    "step": 2,
    "query": "Hãy tra cứu hồ sơ và trạng thái sàng lọc CV của ứng viên có mã UV9999999.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Không tìm thấy dữ liệu hồ sơ ứng viên có mã 'UV9999999'",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 5 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
