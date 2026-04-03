from services.scanner_service import run_scanner

print("🚀 Running AI Stock Scanner...")

results = run_scanner()

if results:
    for r in results:
        print(r)
else:
    print("❌ No signal found")
