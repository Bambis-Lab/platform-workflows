from pathlib import Path
import re, sys, yaml
root=Path(__file__).resolve().parents[1]/'.github/workflows'
errors=[]
for path in sorted(root.glob('*.yml')):
    text=path.read_text()
    try: yaml.safe_load(text)
    except Exception as exc: errors.append(f'{path.name}: invalid YAML: {exc}')
    if 'timeout-minutes:' not in text: errors.append(f'{path.name}: missing timeout')
    if not re.search(r'^permissions:\n\s+contents: read',text,re.M): errors.append(f'{path.name}: permissions must default to contents: read')
    for ref in re.findall(r'uses:\s*([^\s]+)',text):
        if not ref.startswith('./') and not re.fullmatch(r'[^@]+@[0-9a-f]{40}',ref): errors.append(f'{path.name}: action not SHA pinned: {ref}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'WORKFLOW_POLICY=PASS workflows={len(list(root.glob("*.yml")))}')
