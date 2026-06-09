from getpass import getpass
from analyzer import analyze_password

print("\n=== FortiPhrase ===\n")

password = getpass("Enter password: ")

result = analyze_password(password)

print(f"\nScore: {result['score']}/100")
print(
    f"Entropy: {result['entropy']} bits "
    f"({result['entropy_rating']})"
)
print(f"Strength: {result['strength']}")


print("\nIssues:")
for issue in result["issues"]:
    print(f"- {issue}")

print("\nSuggestions:")
for suggestion in result["suggestions"]:
    print(f"- {suggestion}")