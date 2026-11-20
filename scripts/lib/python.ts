// The Python 3 interpreter to spawn. On Windows `python3` is usually the Microsoft Store stub (exit 49, no Pillow), and
// the real interpreter is `python` (2026-11-17, figma-cut.ts failed silently on a Windows machine). CASEBOOK_PYTHON
// overrides both.
export const PY = process.env.CASEBOOK_PYTHON || (process.platform === 'win32' ? 'python' : 'python3');
