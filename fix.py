import subprocess
result = subprocess.run(['git', 'ls-files'], capture_output=True)
files = result.stdout.decode('utf-8').strip().split('\n')
pngs = [f for f in files if f.endswith('.png')]
print(f"찾은 PNG: {len(pngs)}개")
for f in pngs:
    r = subprocess.run(['git', 'rm', '--cached', f])
    print(f, r.returncode)
