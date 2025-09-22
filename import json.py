import json

from datetime import datetime



class PersonalInfoManager:

    """个人信息管理器"""

    

    def __init__(self):

        """初始化"""

        self.users = []

        self.current_user = None

    

    def create_user(self):

        """创建新用户"""

        print("\n创建新用户")

        print("-" * 40)

        

        # 收集基本信息

        name = input("姓名：")

        age = self.get_valid_age()

        email = input("Email：")

        

        # 收集学习目标

        print("\n学习目标（选择一个）：")

        goals = ["AI工程师", "数据科学家", "全栈开发", "研究员", "其他"]

        for i, goal in enumerate(goals, 1):

            print(f"{i}. {goal}")

        

        choice = input("选择（1-5）：")

        goal = goals[int(choice)-1] if choice.isdigit() and 1 <= int(choice) <= 5 else "其他"

        

        # 创建用户字典

        user = {

            "id": len(self.users) + 1,

            "name": name,

            "age": age,

            "email": email,

            "goal": goal,

            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "study_hours": 0,

            "completed_lessons": []

        }

        

        self.users.append(user)

        self.current_user = user

        print(f"\n✅ 用户 {name} 创建成功！")

        return user

    

    def get_valid_age(self):

        """获取有效的年龄输入"""

        while True:

            age_input = input("年龄：")

            if age_input.isdigit():

                age = int(age_input)

                if 10 <= age <= 100:

                    return age

            print("请输入有效的年龄（10-100）")

    

    def display_user_info(self, user=None):

        """显示用户信息"""

        if user is None:

            user = self.current_user

        

        if user is None:

            print("没有当前用户")

            return

        

        print("\n" + "="*50)

        print(" 用户信息卡 ".center(50))

        print("="*50)

        print(f"ID: {user['id']}")

        print(f"姓名：{user['name']}")

        print(f"年龄：{user['age']}岁")

        print(f"Email：{user['email']}")

        print(f"学习目标：{user['goal']}")

        print(f"注册时间：{user['created_at']}")

        print(f"学习时长：{user['study_hours']}小时")

        print(f"完成课程：{len(user['completed_lessons'])}节")

        print("="*50)

    

    def record_study_time(self):

        """记录学习时间"""

        if self.current_user is None:

            print("请先创建或选择用户")

            return

        

        hours_input = input("今天学习了几小时？")

        try:

            hours = float(hours_input)

            self.current_user['study_hours'] += hours

            print(f"✅ 记录成功！总学习时长：{self.current_user['study_hours']}小时")

        except ValueError:

            print("请输入有效的数字")

    

    def mark_lesson_complete(self):

        """标记课程完成"""

        if self.current_user is None:

            print("请先创建或选择用户")

            return

        

        lesson = input("完成的课程名称：")

        self.current_user['completed_lessons'].append({

            "lesson": lesson,

            "date": datetime.now().strftime("%Y-%m-%d")

        })

        print(f"✅ 课程 '{lesson}' 标记为已完成！")

    

    def show_progress(self):

        """显示学习进度"""

        if self.current_user is None:

            print("请先创建或选择用户")

            return

        

        print("\n" + "="*50)

        print(" 学习进度报告 ".center(50))

        print("="*50)

        

        user = self.current_user

        print(f"学员：{user['name']}")

        print(f"目标：{user['goal']}")

        print(f"总学习时长：{user['study_hours']}小时")

        

        # 进度条

        target_hours = 100  # 目标100小时

        progress = min(user['study_hours'] / target_hours * 100, 100)

        bar_length = 30

        filled_length = int(bar_length * progress // 100)

        bar = '█' * filled_length + '░' * (bar_length - filled_length)

        

        print(f"\n进度：[{bar}] {progress:.1f}%")

        print(f"距离100小时目标还需：{max(0, target_hours - user['study_hours']):.1f}小时")

        

        # 已完成课程

        if user['completed_lessons']:

            print(f"\n已完成课程（{len(user['completed_lessons'])}节）：")

            for i, lesson in enumerate(user['completed_lessons'][-5:], 1):  # 显示最近5节

                print(f"  {i}. {lesson['lesson']} - {lesson['date']}")

        

        print("="*50)

    

    def save_data(self):

        """保存数据到文件"""

        filename = "user_data.json"

        try:

            with open(filename, 'w', encoding='utf-8') as f:

                json.dump(self.users, f, ensure_ascii=False, indent=2)

            print(f"✅ 数据已保存到 {filename}")

        except Exception as e:

            print(f"保存失败：{e}")

    

    def load_data(self):

        """从文件加载数据"""

        filename = "user_data.json"

        try:

            with open(filename, 'r', encoding='utf-8') as f:

                self.users = json.load(f)

            print(f"✅ 从 {filename} 加载了 {len(self.users)} 个用户")

            if self.users:

                self.current_user = self.users[-1]

        except FileNotFoundError:

            print("没有找到保存的数据文件")

        except Exception as e:

            print(f"加载失败：{e}")

    

    def run(self):

        """运行主程序"""

        print("""

╔════════════════════════════════════════╗

║     个人信息管理系统 v1.0              ║

║     Python第一周综合练习               ║

╚════════════════════════════════════════╝

        """)

        

        # 尝试加载已有数据

        self.load_data()

        

        while True:

            print("\n" + "="*40)

            print("主菜单")

            print("="*40)

            print("1. 创建新用户")

            print("2. 显示用户信息")

            print("3. 记录学习时间")

            print("4. 标记课程完成")

            print("5. 显示学习进度")

            print("6. 保存数据")

            print("7. 加载数据")

            print("0. 退出")

            

            choice = input("\n请选择（0-7）：")

            

            if choice == '1':

                self.create_user()

            elif choice == '2':

                self.display_user_info()

            elif choice == '3':

                self.record_study_time()

            elif choice == '4':

                self.mark_lesson_complete()

            elif choice == '5':

                self.show_progress()

            elif choice == '6':

                self.save_data()

            elif choice == '7':

                self.load_data()

            elif choice == '0':

                print("\n保存数据中...")

                self.save_data()

                print("再见！继续努力学习！👋")

                break

            else:

                print("无效选择，请重试")



# 独立函数练习

def calculate_study_efficiency(total_hours, completed_lessons):

    """计算学习效率"""

    if total_hours == 0:

        return 0

    return completed_lessons / total_hours



def generate_certificate(name, course="Python基础"):

    """生成结业证书"""

    certificate = f"""

    {'='*50}

    {'结业证书'.center(50)}

    {'='*50}

    

    兹证明

    

    {name} 同学

    

    成功完成了《{course}》课程的学习

    

    颁发日期：{datetime.now().strftime('%Y年%m月%d日')}

    

    {'='*50}

    """

    return certificate



if __name__ == "__main__":

    # 运行主程序

    manager = PersonalInfoManager()

    manager.run()

    

    # 或者测试独立函数

    # print(generate_certificate("张三"))