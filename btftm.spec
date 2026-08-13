Name:           btftm
Version:        1.0.2
Release:        1%{?dist}
Summary:        One-line summary of the package

License:        BSD-3-Clause
URL:            https://qartifactory-edge.qualcomm.com
# Source0's filename must match the entry in `sources`. On a cache miss the
# build downloads this URL, so keep it pointing at a fetchable upstream tarball.
# %{name} and %{version} are expanded, so bumping Version: is usually all you need.
Source0:        https://qartifactory-edge.qualcomm.com/ui/native/qsc_releases/software/chip/component/bt-performant.qclinux.0.0/260604/prebuilt_resolute/btftm_1.0.2_arm64.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
btftm rmp generate

%prep
%autosetup -p1 -n data

%build
# Prebuilt binaries — no compilation step required.

%install
install -d %{buildroot}%{_libdir}/bin
cp -a btdaig/arm64/usr/bin/. %{buildroot}%{_libdir}/bin/

%files
{_libdir}/bin
%license LICENSE
%doc README.md
%{_bindir}/mypackage

%changelog
* Mon Aug 13 2026 geyi <geyi@qti.qualcomm.com> - 1.0.2-1
- Initial package
