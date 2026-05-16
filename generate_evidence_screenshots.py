from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap


BASE_DIR = Path(__file__).parent
SCREENSHOT_DIR = BASE_DIR / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)


def _load_font(size: int):
    font_candidates = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
    ]
    for candidate in font_candidates:
        candidate_path = Path(candidate)
        if candidate_path.exists():
            return ImageFont.truetype(str(candidate_path), size)
    return ImageFont.load_default()


def render_text_image(title: str, lines: list[str], output_file: Path) -> None:
    width = 1800
    padding = 50
    line_height = 34
    title_height = 58
    content_height = max(1, len(lines)) * line_height
    height = padding * 2 + title_height + content_height

    image = Image.new("RGB", (width, height), color=(18, 24, 33))
    draw = ImageDraw.Draw(image)
    title_font = _load_font(36)
    body_font = _load_font(24)

    draw.text((padding, padding), title, fill=(220, 236, 255), font=title_font)
    y = padding + title_height
    for line in lines:
        draw.text((padding, y), line, fill=(232, 240, 252), font=body_font)
        y += line_height

    image.save(output_file)


def read_wrapped_lines(path: Path, width: int = 120) -> list[str]:
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    wrapped = []
    for line in raw_lines:
        if not line.strip():
            wrapped.append("")
            continue
        wrapped.extend(textwrap.wrap(line, width=width) or [""])
    return wrapped


def main() -> None:
    access_table = BASE_DIR / "ACCESS_REVIEW_TABLE.md"
    exception_log = BASE_DIR / "EXCEPTION_LOG.md"
    remediation = BASE_DIR / "REMEDIATION_TRACKER.md"
    findings = BASE_DIR / "FINDINGS.md"

    render_text_image(
        "Access Review Table",
        read_wrapped_lines(access_table),
        SCREENSHOT_DIR / "01-access-review-table.png",
    )

    render_text_image(
        "Exception Log",
        read_wrapped_lines(exception_log),
        SCREENSHOT_DIR / "02-exception-log.png",
    )

    render_text_image(
        "Remediation Tracker",
        read_wrapped_lines(remediation),
        SCREENSHOT_DIR / "03-remediation-tracker.png",
    )

    table_lines = access_table.read_text(encoding="utf-8").splitlines()
    modify_lines = [line for line in table_lines if "Modify" in line]
    remove_lines = [line for line in table_lines if "Remove" in line]

    render_text_image(
        "Modify Decision Example",
        modify_lines,
        SCREENSHOT_DIR / "04-modify-example.png",
    )

    render_text_image(
        "Remove Decision Example",
        remove_lines,
        SCREENSHOT_DIR / "05-remove-example.png",
    )

    findings_lines = findings.read_text(encoding="utf-8").splitlines()
    summary_slice = []
    in_key_findings = False
    for line in findings_lines:
        if line.strip().startswith("## Key Findings"):
            in_key_findings = True
        if in_key_findings:
            summary_slice.append(line)
        if line.strip().startswith("## Risk Summary"):
            break

    render_text_image(
        "Findings Summary",
        summary_slice,
        SCREENSHOT_DIR / "06-findings-summary.png",
    )


if __name__ == "__main__":
    main()
