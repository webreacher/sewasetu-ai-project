import requests
from personas import PERSONAS

BASE_URL = "http://localhost:8000"

def run_tests():
    print("Running automated citizen evaluation suite...")
    for p in PERSONAS:
        resp = requests.post(f"{BASE_URL}/api/internal/citizen/apply", json={
            "mobile": p["mobile"],
            "applicant_name": p["name"],
            "dob": p["dob"],
            "gender": p["gender"],
            "marital_status": p["marital_status"],
            "village": p["village"],
            "block": p["block"],
            "bank_account": p["bank_account"],
            "ifsc": p["ifsc"],
            "doc_path": "/var/sewasetu/uploads/proof.pdf"
        })
        print(f"Persona {p['name']} -> Status: {resp.status_code}, Resp: {resp.json()}")

if __name__ == "__main__":
    run_tests()