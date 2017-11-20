import logging
import argparse
from obnl.wrapper.node import WrapperNode

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("tool_pass")
    parser.add_argument("obnl_pass")

    args = parser.parse_args()

    WrapperNode.activate_console_logging(logging.DEBUG)
    w = WrapperNode(args.host, "backend_vhost", "tool", args.tool_pass, args.obnl_pass, "wrapper.json", "scheduler.json")
    w.start()
1