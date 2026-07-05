# mes.medicalframe.ai deployment

## GitHub Pages

- Repository: `https://github.com/MedicalFrame/mes.medicalframe.ai`
- Pages source: `main` branch, repository root
- Custom domain: `mes.medicalframe.ai`
- CNAME file: `CNAME`

## DNS

Set this record at the DNS provider for `medicalframe.ai`:

```text
Type: CNAME
Name: mes
Value: medicalframe.github.io
```

After DNS resolves, enable HTTPS enforcement in GitHub Pages if it is not enabled automatically.

## Verification

```bash
dig CNAME mes.medicalframe.ai
curl -I https://mes.medicalframe.ai
```

Before DNS resolves, verify the site through the GitHub Pages URL:

```bash
curl -I https://medicalframe.github.io/mes.medicalframe.ai/
```
