import argparse,os,sys,time,shutil

parser=argparse.ArgumentParser(description="To files older than N days")
parser.add_argument('--path', help="path /var/log/hadoop")
parser.add_argument('--days', help="only integer value and default value is 7", type=int, default=7)
args= parser.parse_args()
now = time.time()

if not os.path.exists(args.path):
  print("{} doesn't exists".format(args.path))
  sys.exit(1)

for f in os.listdir(args.path):
  if os.stat(os.path.join(args.path,f)).st_mtime < now - args.days * 86400:
    os.remove(os.path.join(args.path,f))
