from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

INVITATION_IMAGE = PROJECT_DIR / "input" / "invitation.png"
EXCEL_FILE = PROJECT_DIR / "input" / "recipients.xlsx"
FONT_PATH = Path("./fonts/Rakkas/Rakkas-Regular.ttf")

OUTPUT_DIR = PROJECT_DIR / "output"
PERSONALIZED_DIR = OUTPUT_DIR / "personalized"
LOG_FILE = OUTPUT_DIR / "logs" / "send_log.csv"
PREVIEW_FILE = OUTPUT_DIR / "preview.png"

# Offsets from the exact center of the image, in pixels.
# Positive X moves right, positive Y moves down.
NAME_OFFSET_X = 0
NAME_OFFSET_Y = 235
NAME_COLOR = "#000000"
NAME_ANCHOR = "mm"

# {name} is replaced with the recipient's name. This is sent as the image caption.
DEFAULT_MESSAGE = """السلام عليكم ورحمة الله وبركاته..

{name}، لأن لكل حكاية أشخاصاً يضيفون إليها معنى، يسعدنا أن تكونوا معنا في بداية حكايتنا الجديدة، حيث لا يكتمل البناء إلا بعزائم صادقة وأيدٍ تجتمع على هدفٍ واحد. 💫

اليوم، نبدأ معاً فصلاً جديداً من حكايةٍ امتدّت بجهودٍ مخلصة، ونطمح أن تكون فصولها القادمة أكثر عطاءً وأثراً.

ينطلق اتحادكم بروح متجددة ورؤية واضحة، مؤمناً بأن التغيير الحقيقي لا يُصنع إلا بسواعد الطلاب، وبعزائمهم التي لا تعرف الفتور.

في «بداية الحكاية 4»، ندعوكم لنكون معاً في هذه البداية، لا مجرد حاضرين نشهدها، بل شركاء في صناعتها وصنّاعاً لأثرها. فكم من فكرة بدأت بخطوة، وكم من أثر عظيم صنعته يدٌ آمنت أن بإمكانها أن تُحدث فرقاً.

📍 المكان: قاعة Seminer 2
📆 الزمان: الثلاثاء 27/10/2026
⏰ الوقت: الساعة 15:00"""

PAGE_TIMEOUT_MS = 45000

# Random pause between recipients, in seconds.
MIN_DELAY_SECONDS = 20
MAX_DELAY_SECONDS = 45

FONT_SIZE = 90           # starting (maximum) size, used for short names
MIN_FONT_SIZE = 60        # never go smaller than this
MAX_NAME_WIDTH_RATIO = 0.32  # name may use at most 32% of the image width


