FailedLogins = 0
SuccessLogins = 0
attempts = []
with open('log.txt', 'r') as file:
    for line in file:
        attempts.append(line.rstrip())

        if "failed" in line.lower():
            FailedLogins += 1
        else:
            SuccessLogins += 1
print(f"There were {FailedLogins} failed logins.")
print(f"There were {SuccessLogins} successful logins.")
for attempt in attempts:
    print(attempt)