import argparse
import os
import shutil
import subprocess

BASE_DIR = "examples"


def prepare(work_dir, ex, copy_all):
    if os.path.exists(work_dir):
        shutil.rmtree(work_dir)
    os.makedirs(work_dir)
    shutil.copy(os.path.join(BASE_DIR, ex, "failure", "task.py"), work_dir)
    shutil.copy(os.path.join(BASE_DIR, ex, "description", "robot.py"), os.path.join(work_dir, "test.py"))
    if copy_all:
        shutil.copy(os.path.join(BASE_DIR, ex, "correct", "task.py"), os.path.join(work_dir, "task-correct.py"))
        shutil.copy(os.path.join(BASE_DIR, ex, "failure2", "task.py"), os.path.join(work_dir, "task-failing.py"))
        shutil.copy(os.path.join(BASE_DIR, ex, "failure", "task.py"), os.path.join(work_dir, "task-buggy.py"))


def show_description(ex):
    with open(os.path.join(BASE_DIR, ex, "description", "task-description.md"), "r", encoding="utf-8") as fp:
        print(fp.read())


def show_example(ex):
    if not os.path.exists(os.path.join(BASE_DIR, ex, "description", "example.md")):
        print("The example does not exist!")
        return
    with open(os.path.join(BASE_DIR, ex, "description", "example.md"), "r", encoding="utf-8") as fp:
        print(fp.read())


def run_tests(work_dir):
    if not os.path.exists(os.path.join(work_dir, "test.py")):
        print("The test file does not exist!")
        print("Run prepare first!")
    cp = subprocess.run(["python", os.path.join(work_dir, "test.py")], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    print(cp.stdout)
    print(cp.stderr)
    return cp.returncode


def prepare_fix(work_dir, ex, failing=False):
    if failing:
        shutil.copy(os.path.join(BASE_DIR, ex, "failure2", "task.py"), work_dir)
    else:
        shutil.copy(os.path.join(BASE_DIR, ex, "correct", "task.py"), work_dir)


def main(args):
    if not args.ex.startswith("ex"):
        args.ex = "ex" + args.ex
    if args.prepare:
        prepare(args.work, args.ex, args.copy_all)
    if args.show_description:
        show_description(args.ex)
    if args.show_example:
        show_example(args.ex)
    if args.fix:
        prepare_fix(args.work, args.ex)
    if args.failing:
        prepare_fix(args.work, args.ex, failing=True)
    if args.run:
        run_tests(args.work)
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--work", type=str, default="work", help="The working directory in which the example will be arranged.")
    parser.add_argument("-e", "--ex", type=str, default="ex1", help="The identifier of the example the application currently works with. For example, 'ex12' or '12'.")
    parser.add_argument("--show-description", action="store_true", help="Prints the description to the standard output.")
    parser.add_argument("--show-example", action="store_true", help="Prints the example to the standard output.")
    parser.add_argument("--prepare", action="store_true", help="Prepares the work directory with the given example. It copies the buggy code snippet, as well as the unit tests of the example into the work directory.")
    parser.add_argument("--fix", action="store_true", help="Copies the correct solution to the work directory.")
    parser.add_argument("--failing", action="store_true", help="Copies the failed solution (which differs from the buggy version) to the work directory.")
    parser.add_argument("--copy_all", action="store_true", default=False, help="Copy all resources to the working directory")
    parser.add_argument("--run", action="store_true", default=False, help="Runs the unit tests. It outputs both the standard output and standard error output to the standard output.")
    args = parser.parse_args()
    main(args)
