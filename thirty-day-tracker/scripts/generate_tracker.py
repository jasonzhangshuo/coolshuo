#!/usr/bin/env python3
"""
生成30天追踪表

用法:
    python generate_tracker.py --start 2026-01-21
    python generate_tracker.py --start 2026-01-21 --format markdown
    python generate_tracker.py --start 2026-01-21 --format csv
"""

import argparse
from datetime import datetime, timedelta

def generate_markdown_tracker(start_date: datetime) -> str:
    """生成Markdown格式追踪表"""
    lines = [
        "# 30天习惯追踪表",
        "",
        f"开始日期: {start_date.strftime('%Y-%m-%d')}",
        f"结束日期: {(start_date + timedelta(days=29)).strftime('%Y-%m-%d')}",
        "",
        "## XP规则",
        "- 锚点1（晨间定课）: 10 XP",
        "- 锚点2（身体运动）: 10 XP",
        "- 锚点3（睡前回顾）: 10 XP",
        "- 半山内容发布: 20 XP",
        "- 法义90分钟: 20 XP",
        "- 对治罪: 10 XP",
        "- 每日满分: 80 XP | 30天满分: 2400 XP",
        "",
        "## 等级",
        "- 新手: 0-599 XP",
        "- 学徒: 600-1199 XP",
        "- 熟练者: 1200-1799 XP",
        "- 大师: 1800-2400 XP",
        "",
        "## 追踪表",
        "",
        "| Day | 日期 | 锚1 | 锚2 | 锚3 | 半山 | 法义 | 对治罪 | XP | 累计 |",
        "|-----|------|-----|-----|-----|------|------|--------|-----|------|",
    ]

    for day in range(1, 31):
        date = start_date + timedelta(days=day - 1)
        date_str = date.strftime("%m.%d")
        lines.append(f"| {day} | {date_str} | ☐ | ☐ | ☐ | ☐ | ☐ | | /80 | |")

    lines.extend([
        "",
        "## 每周复盘",
        "",
        "### 第1周复盘",
        "- 完成情况:",
        "- 最大收获:",
        "- 需要调整:",
        "",
        "### 第2周复盘",
        "- 完成情况:",
        "- 最大收获:",
        "- 需要调整:",
        "",
        "### 第3周复盘",
        "- 完成情况:",
        "- 最大收获:",
        "- 需要调整:",
        "",
        "### 第4周复盘",
        "- 完成情况:",
        "- 最大收获:",
        "- 需要调整:",
        "",
        "## 30天总结",
        "",
        "最终XP: ___/2400",
        "最终等级: ___",
        "",
        "### 三个最大的变化",
        "1. ",
        "2. ",
        "3. ",
        "",
        "### 要继续保持的习惯",
        "1. ",
        "2. ",
        "3. ",
        "",
    ])

    return "\n".join(lines)

def generate_csv_tracker(start_date: datetime) -> str:
    """生成CSV格式追踪表"""
    lines = ["Day,日期,锚1,锚2,锚3,半山,法义,对治罪,XP,累计"]

    for day in range(1, 31):
        date = start_date + timedelta(days=day - 1)
        date_str = date.strftime("%Y-%m-%d")
        lines.append(f"{day},{date_str},,,,,,,0,0")

    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="生成30天追踪表")
    parser.add_argument("--start", type=str, required=True, help="开始日期 (YYYY-MM-DD)")
    parser.add_argument("--format", type=str, default="markdown", choices=["markdown", "csv"], help="输出格式")
    parser.add_argument("--output", type=str, help="输出文件路径")

    args = parser.parse_args()

    start_date = datetime.strptime(args.start, "%Y-%m-%d")

    if args.format == "markdown":
        content = generate_markdown_tracker(start_date)
        default_ext = ".md"
    else:
        content = generate_csv_tracker(start_date)
        default_ext = ".csv"

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"追踪表已保存到: {args.output}")
    else:
        print(content)

if __name__ == "__main__":
    main()
