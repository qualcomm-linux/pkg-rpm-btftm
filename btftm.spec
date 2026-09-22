%global debug_package %{nil}
Name:           btftm
Version:        1.0.3
Release:        1%{?dist}
Summary:        Qualcomm Bluetooth firmware test and management binary
License:        Qualcomm.nologin.binaries.license
URL:            https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/bt-performant.qclinux.0.0
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/bt-performant.qclinux.0.0/260821/prebuilt_resolute/%{name}_%{version}_arm64.tar.gz
ExclusiveArch:  aarch64

%description
btftm is a prebuilt Qualcomm Bluetooth firmware test and management
application for Qualcomm Linux platforms.

%prep
%autosetup -n data

%build
# Prebuilt binaries -- no compilation required.

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_docdir}/btftmdaemon
install -m 0755 btftmdaemon/arm64/usr/bin/btftmdaemon \
    %{buildroot}%{_bindir}/btftmdaemon
install -m 0644 btftmdaemon/arm64/usr/share/doc/btftmdaemon/changelog.gz \
    %{buildroot}%{_docdir}/btftmdaemon/changelog.gz

%files
%doc %{_docdir}/btftmdaemon/changelog.gz
%{_bindir}/btftmdaemon

%changelog
* Mon Aug 25 2026 geyi <geyi@qti.qualcomm.com> - 1.0.3-1
- Initial RPM packaging of btftm prebuilt binary
