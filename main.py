from analyzer import analyze_password

print("\n=== FortiPhrase ===\n")

password = input("Enter password: ")

result = analyze_password(password)

print(f"\nScore: {result['score']}/100")
print(f"Strength: {result['strength']}")

print("\nIssues:")
for issue in result["issues"]:
    print(f"- {issue}")

print("\nSuggestions:")
for suggestion in result["suggestions"]:
    print(f"- {suggestion}")