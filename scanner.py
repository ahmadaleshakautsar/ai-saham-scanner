from services.scanner_service import run_scanner

results = run_scanner()

for r in results:
    print(r)
