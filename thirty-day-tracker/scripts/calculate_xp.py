#!/usr/bin/env python3
"""
计算30天追踪的XP和等级

用法:
    python calculate_xp.py --anchor1 --anchor2 --anchor3 --content --study --sin
    python calculate_xp.py --total 450
"""

import argparse

# XP 规则
XP_RULES = {
    "anchor1": 10,   # 晨间定课
    "anchor2": 10,   # 身体运动
    "anchor3": 10,   # 睡前回顾
    "content": 20,   # 半山内容发布
    "study": 20,     # 法义90分钟
    "sin": 10,       # 对治1条罪
}

# 等级系统
LEVELS = [
    (0, 599, "新手"),
    (600, 1199, "学徒"),
    (1200, 1799, "熟练者"),
    (1800, 2400, "大师"),
]

def calculate_daily_xp(tasks: dict) -> int:
    """计算单日XP"""
    total = 0
    for task, completed in tasks.items():
        if completed and task in XP_RULES:
            total += XP_RULES[task]
    return min(total, 80)  # 每日最高80

def get_level(total_xp: int) -> str:
    """根据总XP获取等级"""
    for min_xp, max_xp, level in LEVELS:
        if min_xp <= total_xp <= max_xp:
            return level
    return "大师" if total_xp > 2400 else "新手"

def get_progress_bar(total_xp: int, width: int = 30) -> str:
    """生成进度条"""
    percentage = min(total_xp / 2400, 1.0)
    filled = int(width * percentage)
    empty = width - filled
    return "█" * filled + "░" * empty

def main():
    parser = argparse.ArgumentParser(description="计算30天追踪XP")
    parser.add_argument("--anchor1", action="store_true", help="完成晨间定课")
    parser.add_argument("--anchor2", action="store_true", help="完成身体运动")
    parser.add_argument("--anchor3", action="store_true", help="完成睡前回顾")
    parser.add_argument("--content", action="store_true", help="发布半山内容")
    parser.add_argument("--study", action="store_true", help="完成法义90分钟")
    parser.add_argument("--sin", action="store_true", help="对治1条罪")
    parser.add_argument("--total", type=int, default=0, help="之前累计的XP")
    parser.add_argument("--day", type=int, default=1, help="当前是第几天")

    args = parser.parse_args()

    # 计算今日XP
    tasks = {
        "anchor1": args.anchor1,
        "anchor2": args.anchor2,
        "anchor3": args.anchor3,
        "content": args.content,
        "study": args.study,
        "sin": args.sin,
    }

    daily_xp = calculate_daily_xp(tasks)
    total_xp = args.total + daily_xp
    level = get_level(total_xp)
    progress_bar = get_progress_bar(total_xp)
    percentage = min(total_xp / 2400 * 100, 100)

    print(f"\n📊 Day {args.day}/30 XP 统计")
    print("=" * 40)
    print(f"\n今日完成:")
    for task, completed in tasks.items():
        status = "✅" if completed else "☐"
        xp = XP_RULES[task] if completed else 0
        names = {
            "anchor1": "晨间定课",
            "anchor2": "身体运动",
            "anchor3": "睡前回顾",
            "content": "半山内容",
            "study": "法义90分钟",
            "sin": "对治罪",
        }
        print(f"  {status} {names[task]}: +{xp} XP")

    print(f"\n今日获得: {daily_xp}/80 XP")
    print(f"累计XP: {total_xp}/2400")
    print(f"\n进度: {progress_bar} {percentage:.1f}%")
    print(f"当前等级: {level}")
    print()

if __name__ == "__main__":
    main()
