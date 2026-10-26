# WhatsApp Invitation Bot (Linux Mint)

This project:
1. Reads recipients from an Excel workbook.
2. Writes each person's name onto a copy of your invitation image.
3. Lets you preview/adjust the name position, font size, color, and alignment.
4. Can open WhatsApp Web conversations and prepare/send messages with the personalized image.

**Important:** WhatsApp Web's interface can change, and browser automation may be unreliable or may trigger account restrictions. Use only for recipients who expect the invitation. Start with one test recipient. The `send` mode is intentionally confirmation-based: you must confirm each recipient in the terminal before the script proceeds.

## 1. Set up (Linux Mint)

```bash
cd whatsapp_invitation_bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

If Playwright reports missing Linux libraries:
```bash
playwright install-deps chromium
```

## 2. Add your files

- Put the original invitation image at `input/invitation.png` (or change `INVITATION_IMAGE` in `config.py`).
- Put your font file (`.ttf` or `.otf`) at `fonts/your-font.ttf`, then set `FONT_PATH` in `config.py`.
- `input/recipients.xlsx` is included as a template. Replace the example row and keep these column headers in row 1:
  - `name`
  - `phone`

The bot reads recipients from Excel only; no CSV file is used. The WhatsApp message is defined once in `DEFAULT_MESSAGE` in `config.py` and is used for every recipient. The `{name}` placeholder is replaced with each recipient's name. Do not add a `message` column.

Phone numbers should include country code, digits only or with a leading `+`, e.g. `+905xxxxxxxxx`. Do not use Excel numeric cells for phone numbers; store them as text so leading digits are preserved.

## 3. Preview a name

```bash
python main.py preview --name "عبد الرحمن"
```

Open `output/preview.png`. Adjust `NAME_X`, `NAME_Y`, `FONT_SIZE`, `NAME_COLOR`, and `NAME_ANCHOR` in `config.py`. Coordinates are pixels measured from the top-left corner of the image.

`NAME_ANCHOR` can be `mm` (center), `rm` (right-middle), or `lm` (left-middle). For Arabic names, `rm` or `mm` is often a good starting point depending on the design. Pillow's `anchor` is alignment, not a text-direction switch; Arabic shaping and bidirectional handling are applied separately.

## 4. Generate all personalized images without sending

```bash
python main.py prepare
```

Images are saved under `output/personalized/`. The original invitation is not modified.

## 5. Send using WhatsApp Web

```bash
python main.py send
```

The first run opens a Chromium browser. Scan the QR code in WhatsApp Web if asked and keep the browser open. For each recipient, the script:
- asks for terminal confirmation,
- opens the conversation,
- sends the personalized image with the configured message.

Test with your own number first. Stop the script with Ctrl+C if anything looks wrong. Do not run multiple copies at once.

## Notes

- Arabic shaping depends on the supplied font containing the required Arabic glyphs.
- A font file is not included; add your own licensed font file.
- If your invitation image has a transparent background, output is saved as PNG. Other image formats are also supported.
- Delivery status is not guaranteed merely because the script clicks a send button. Check WhatsApp Web and the log.


## Existing virtual environment

Virtual environments are not reliably portable between folder paths because some scripts contain absolute paths. To avoid reinstalling packages, the safest option is to keep using your current project folder and replace its `main.py` and `config.py` with the versions in this project. If you choose to use this new folder, you can try copying your existing `.venv` into it, then run `source .venv/bin/activate` and `python -m playwright --version`; if activation or imports fail, the environment will need to be recreated in the new location.
# Whatsapp-bot
