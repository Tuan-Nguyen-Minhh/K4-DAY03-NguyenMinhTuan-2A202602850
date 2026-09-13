"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu hồ sơ ứng viên
    {
        "name": "candidate_query",
        "description": "Tra cứu hồ sơ, vị trí ứng tuyển và thông tin chi tiết của ứng viên bằng mã định danh.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_id": {
                    "type": "string",
                    "description": "Mã định danh ứng viên cần tra cứu (ví dụ: 'UV2026001')"
                },
                "role": {
                    "type": "string",
                    "description": "Vị trí ứng viên ứng tuyển hoặc mong muốn (tùy chọn)"
                }
            },
            "required": ["candidate_id"]
        }
    },
    
    # Tool 2: Đặt lịch và gửi thông báo phỏng vấn
    {
        "name": "schedule_interview",
        "description": "Đặt lịch hẹn phỏng vấn và gửi thông báo cho ứng viên vào hệ thống tuyển dụng.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_id": {
                    "type": "string",
                    "description": "Mã định danh của ứng viên cần đặt lịch (ví dụ: 'UV2026001')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian diễn ra buổi phỏng vấn (ví dụ: '14:00 20/09/2026')"
                },
                "interviewer": {
                    "type": "string",
                    "description": "Tên hoặc chức danh của người phụ trách phỏng vấn (ví dụ: 'Trưởng phòng Tuyển dụng', 'TS. Lê Thị B')"
                },
                "round": {
                    "type": "string",
                    "description": "Vòng phỏng vấn (ví dụ: 'Vòng 1 - Sơ loại', 'Vòng 2 - Kỹ thuật'). Không bắt buộc."
                }
            },
            "required": ["candidate_id", "datetime_str", "interviewer"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "UV2026001": {
        "full_name": "Nguyễn Văn An",
        "applied_role": "Kỹ sư AI / Machine Learning",
        "experience_years": 3,
        "skills": ["Python", "PyTorch", "LLM", "MCP"],
        "email": "an.nguyen@example.com",
        "screening_status": "ĐẠT - Đủ điều kiện phỏng vấn chuyên môn",
        "assigned_interviewer": "Trưởng phòng Kỹ thuật"
    },
    "UV2026002": {
        "full_name": "Trần Thị Bình",
        "applied_role": "Chuyên viên Phân tích Dữ liệu",
        "experience_years": 1,
        "skills": ["SQL", "PowerBI", "Python"],
        "email": "binh.tran@example.com",
        "screening_status": "CHỜ DUYỆT",
        "assigned_interviewer": "Trưởng nhóm Data Analytics"
    }
}


def execute_candidate_query(candidate_id: str, role: str = "") -> str:
    """Thực thi tra cứu hồ sơ ứng viên theo mã định danh"""
    candidate = MOCK_DATABASE.get(candidate_id.strip().upper())
    if candidate:
        return json.dumps({
            "status": "SUCCESS",
            "candidate_id": candidate_id,
            "data": candidate
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu hồ sơ ứng viên có mã '{candidate_id}'"
        }, ensure_ascii=False)


def execute_schedule_interview(candidate_id: str, datetime_str: str, interviewer: str, round: str = "Vòng 1 - Phỏng vấn chuyên môn") -> str:
    """Thực thi đặt lịch và gửi thông báo phỏng vấn"""
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"INT-{candidate_id}-2026",
        "candidate_id": candidate_id,
        "datetime": datetime_str,
        "interviewer": interviewer,
        "round": round,
        "message": f"Đã đặt lịch phỏng vấn thành công cho ứng viên {candidate_id} vào lúc {datetime_str} với {interviewer} ({round}). Thông báo đã được gửi đến ứng viên."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "candidate_query": execute_candidate_query,
    "schedule_interview": execute_schedule_interview
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
