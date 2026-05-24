# Simp Timer

A simple looping countdown timer. Set minutes + seconds, hit **Start**, and it counts down → alarms for 15 seconds → restarts automatically. **Stop** ends the loop.

Single-file static site (`index.html`) — no build step, no dependencies, hosted on GitHub Pages.

## Add to phone home screen

**iOS (Safari):** open the page → Share → **Add to Home Screen** → tap **Add**.
**Android (Chrome):** open the page → ⋮ menu → **Add to Home screen** / **Install app**.

Once installed the icon launches the timer in standalone mode (no browser chrome).

## Notes

- Keep the tab in the foreground — phones throttle background JS.
- First **Start** tap unlocks audio (browser policy).
- Wake Lock is requested where supported, so the screen stays on while the loop is running.

## Re-render icons

Edit `make-icons.py` (Python + Pillow) and re-run:

```bash
python make-icons.py
```
