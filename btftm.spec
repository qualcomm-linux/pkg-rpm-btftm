Name:           btftm
Version:        1.0.3
Release:        1%{?dist}
Summary:        btftm rmp generate

License:        BSD-3-Clause
URL:            https://qartifactory-edge.qualcomm.com
# Source0's filename must match the entry in `sources`. On a cache miss the
# build downloads this URL, so keep it pointing at a fetchable upstream tarball.
# %{name} and %{version} are expanded, so bumping Version: is usually all you need.
Source0:        https://qartifactory-edge.qualcomm.com/ui/native/qsc_releases/software/chip/component/bt-performant.qclinux.0.0/260821/prebuilt_resolute/btftm_1.0.3_arm64.tar.gz

ExclusiveArch:  aarch64

%description
btftm rmp generate

%prep
%autosetup -p1 -n data

%build
# Prebuilt binaries — no compilation step required.

%install
install -d %{buildroot}%{_libdir}/bin
cp -a btftmdaemon/arm64/usr/bin/. %{buildroot}%{_libdir}/bin/

%files
{_libdir}/bin/btftmdaemon



%changelog
* Mon Aug 25 2026 geyi <geyi@qti.qualcomm.com> - 1.0.3-1
- Initial package
