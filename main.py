from argparse import ArgumentParser

def pretrain():
    pass

def finetune():
    pass

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-m", "--mode")
    args = parser.parse_args()
    if args.mode == "pretrain":
        pretrain()
    elif args.mode == "finetune":
        finetune()
    else:
        print("Provide a mode.")