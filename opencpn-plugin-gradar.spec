%global commit 93282fea4a2889f10d0545b58e3fe75c4754f245
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner bdbcat
%global project gradar_pi
%global plugin gradar

Name: opencpn-plugin-%{plugin}
Summary: Garmin radar plugin for OpenCPN
Version: 1.5
Release: 1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Enhances: opencpn%{_isa}

%description
Garmin radar plugin for OpenCPN

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so
