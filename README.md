# SNS Shared Production Repo

Shared repository for CoMindWorks SNS carousel production across Windows and Mac mini Codex sessions.

## Setup On Mac mini

```bash
git clone https://github.com/kinjungho-sudo/sns_new.git ~/Downloads/comindworks_ai/projects/SNS
cd ~/Downloads/comindworks_ai/projects/SNS
bash scripts/install-codex-skills.sh
```

## Setup On Windows

```powershell
git clone https://github.com/kinjungho-sudo/sns_new.git D:\SNS
cd D:\SNS
.\scripts\install-codex-skills.ps1
```

## Working Rule

- Put new shared carousel packages under `carousels/shared/YYYY/MM/<project-name>/`.
- Keep local-only archives outside Git or under ignored folders.
- Commit source files, final PNGs, contact sheets, ZIPs, captions, and validation scripts needed to reproduce the package.
- Do not commit Codex auth/session files or secrets.

## Git LFS

Images, videos, archives, and PDF exports are tracked with Git LFS via `.gitattributes`.
