# This script runs the full pipeline automatically

import subprocess


def run_script(script_name):
    print(f"\nRunning {script_name}...")
    subprocess.run(["python", script_name], check=True)


def main():

    run_script("save_memo.py")
    run_script("generate_agent.py")
    run_script("version_update.py")
    run_script("generate_diff.py")

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()