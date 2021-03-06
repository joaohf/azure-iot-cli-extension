# Microsoft Azure IoT Extension for Azure CLI 2.0

## Installation Troubleshooting

**Problem**

After installing Azure CLI in my supported Linux environment, I try to install the extension via `az extension add --name azure-cli-iot-ext` but I get an error that looks like:

```diff
- ImportError: libffi.so.5: cannot open shared object file: No such file or directory
```

**Solution**

Make sure you install the right distribution of Azure CLI that is compatible with your platform.

For example using the recommended installation path of [Linux via apt](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest), validate that your `/etc/apt/sources.list.d/azure-cli.list` file has the proper distribution identifier.

On the Ubuntu environment provided with the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) the sources list file will have an entry that will be tagged with 'xenial':

`deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ xenial main`