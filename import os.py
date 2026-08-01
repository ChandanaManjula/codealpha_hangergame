import os
import shutil
import re
import requests

def run_pipeline():
    base_dir = "automation_center"
    logs_dir = os.path.join(base_dir, "incoming_logs")
    archive_dir = os.path.join(base_dir, "archive")
    summary_file_path = os.path.join(base_dir, "final_summary.txt")

    print("Initializing directory structures...")
    os.makedirs(logs_dir, exist_ok=True)
    os.makedirs(archive_dir, exist_ok=True)

    print("Fetching server log URLs from API...")
    try:
        api_url = "https://typicode.com" 
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        print("API Status: Connection Successful.")
    except requests.exceptions.RequestException as e:
        print(f"Network error skipped: {e}")

    sample_data = """
    [2026-08-01 10:15:32] ERROR: Database connection failed for user_id:8912
    [2026-08-01 10:17:11] INFO: User login succeeded
    [2026-08-01 10:22:45] ERROR: Timeout on payment gateway for user_id:4421
    """
    raw_log_path = os.path.join(logs_dir, "raw_server_log.txt")
    with open(raw_log_path, "w", encoding="utf-8") as file:
        file.write(sample_data.strip())

    print("Scanning log data for specific system errors...")
    error_pattern = re.compile(r"ERROR:\s*(.*?)\s*for user_id:(\d+)")
    extracted_incidents = []

    if os.path.exists(raw_log_path):
        with open(raw_log_path, "r", encoding="utf-8") as log_file:
            for line in log_file:
                match = error_pattern.search(line)
                if match:
                    error_msg = match.group(1)
                    user_id = match.group(2)
                    extracted_incidents.append(f"User {user_id} encountered: {error_msg}\n")

    print("Writing extracted data summaries to summary file...")
    with open(summary_file_path, "w", encoding="utf-8") as summary_file:
        summary_file.write("--- AUTOMATED SYSTEM ERROR REPORT ---\n")
        if extracted_incidents:
            summary_file.writelines(extracted_incidents)
        else:
            summary_file.write("No system errors recorded during this window.\n")

    print("Archiving processed logs to historical directories...")
    backup_target = os.path.join(archive_dir, "raw_server_log.bak")
    shutil.move(raw_log_path, backup_target)
    print(f"Pipeline executed successfully. Outputs saved to: {summary_file_path}")

if __name__ == "__main__":
    run_pipeline()
