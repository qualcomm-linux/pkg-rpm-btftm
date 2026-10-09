# btftm

### Introduction

btftm (Bluetooth Factory Test Mode) is a Qualcomm Bluetooth firmware test and
management tool for Qualcomm Linux platforms. It packages the prebuilt
`btftmdaemon` binary used to drive BT RF calibration and non-signalling
conformance testing (BQB/FCC) during manufacturing and bring-up.

### Practical Applications

btftm is used in factory and bring-up environments where the Bluetooth
controller needs to be put into a test/calibration mode outside of normal
protocol operation, for example:
- RF calibration of the Bluetooth radio during board bring-up.
- Non-signalling conformance testing (BQB/FCC) ahead of certification.
- TCP/IP based remote control of the BT controller's test mode from a test
  host.

### Building

The `btftm.spec` file extracts the prebuilt `btftmdaemon` binary from the
vendor-provided tarball and installs it into the appropriate package staging
directories. There is no compilation step; this is a prebuilt-binary package.

### Installation

- `btftmdaemon` dynamically links against `libdiag.so.1`. Install
  [qcom-libdiag](https://github.com/qualcomm-linux/pkg-rpm-libdiag) first,
  otherwise `dnf`/`rpm` will refuse to install `btftm` with a missing
  dependency error.
- Install the package: `sudo dnf install btftm-<version>.el10.aarch64.rpm`
- Once installed, `btftmdaemon` is available at `/usr/bin/btftmdaemon`.

### Testing

```bash
# Confirm the binary resolves libdiag.so.1 and runs
ldd /usr/bin/btftmdaemon
/usr/bin/btftmdaemon --help
```

Run `btftmdaemon` in non-daemon mode (`-n`) with the desired TCP port
(`-p <port>`) to drive factory test commands from a remote test host over
TCP/IP.

### Bug Reporting Guidelines

When reporting bugs, please provide the following details to facilitate
debugging:
- **Platform/SoC Name:** Specify the name of the platform or System on Chip
  (SoC) being used.
- **btftm/qcom-libdiag Versions:** Output of `rpm -qa | grep -E 'btftm|qcom-libdiag'`.
- **Command & Parameters:** The exact `btftmdaemon` invocation and any TCP
  client commands sent to it.
- **Logs:** `dmesg`/`journalctl` output around the time of the failure, and
  any BT snoop logs (`btmon`) captured during the test session.

### License

pkg-rpm-btftm is licensed under the
[BSD-3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html). See
[LICENSE.txt](LICENSE.txt)
for the full license text. The packaged `btftmdaemon` binary itself ships
under Qualcomm's binary license — see `LICENSE.qcom-2` and `NOTICE` in the
installed package.
