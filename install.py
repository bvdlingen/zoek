import argparse
import os


def main():
  """Installs the zoek command."""

  parser = argparse.ArgumentParser(description="Installs the zoek command.")
  parser.add_argument(
      "-f",
      "--force",
      action="store_true",
      help="Force the installation of zoek even if it is already installed.",
  )
  args = parser.parse_args()

  if not os.path.exists("/usr/bin/zoek") or args.force:
    print("Downloading zoek...")
    curl_command = "sudo curl -o /usr/bin/zoek https://raw.githubusercontent.com/bvdlingen/zoek/master/zoek"
    os.system(curl_command)

  print("Setting execute permissions...")
  chmod_command = "sudo chmod +x /usr/bin/zoek"
  os.system(chmod_command)


if __name__ == "__main__":
  main()
