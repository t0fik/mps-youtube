# Created by pyp2rpm-3.2.1
%global pypi_name pafy

Name:           python-%{pypi_name}
Version:        0.5.5
Release:        1%{?dist}
Summary:        Retrieve YouTube content and metadata

License:        LGPLv3
URL:            http://np1.github.io/pafy/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?fedora} < 30
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

BuildRequires:	youtube-dl


%description
 Retreive metadata such as viewcount, duration, rating, author, thumbnail,
keywords Download video or audio at requested resolution / bitrate / format /
filesize Command line tool (ytdl) for downloading directly from the command
line Retrieve the URL to stream the video in a player such as vlc or mplayer
Works with agerestricted videos and nonembeddable videos Small, standalone,
single ...

%package -n     python3-%{pypi_name}
Summary:        Retrieve YouTube content and metadata
Requires:	youtube-dl

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 Retreive metadata such as viewcount, duration, rating, author, thumbnail,
keywords Download video or audio at requested resolution / bitrate / format /
filesize Command line tool (ytdl) for downloading directly from the command
line Retrieve the URL to stream the video in a player such as vlc or mplayer
Works with agerestricted videos and nonembeddable videos Small, standalone,
single ...


%if 0%{?fedora} < 30
%package -n     python2-%{pypi_name}
Summary:        Retrieve YouTube content and metadata
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
 Retreive metadata such as viewcount, duration, rating, author, thumbnail,
keywords Download video or audio at requested resolution / bitrate / format /
filesize Command line tool (ytdl) for downloading directly from the command
line Retrieve the URL to stream the video in a player such as vlc or mplayer
Works with agerestricted videos and nonembeddable videos Small, standalone,
single ...
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%if 0%{?fedora} < 30
PAFY_BACKEND=internal %py2_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
cp %{buildroot}/%{_bindir}/ytdl %{buildroot}/%{_bindir}/ytdl-3
ln -sf %{_bindir}/ytdl-3 %{buildroot}/%{_bindir}/ytdl-%{python3_version}

%if 0%{?fedora} < 30
PAFY_BACKEND=internal %py2_install
cp %{buildroot}/%{_bindir}/ytdl %{buildroot}/%{_bindir}/ytdl-2
ln -sf %{_bindir}/ytdl-2 %{buildroot}/%{_bindir}/ytdl-%{python2_version}
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/ytdl
%{_bindir}/ytdl-3
%{_bindir}/ytdl-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?fedora} < 30
%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/ytdl-2
%{_bindir}/ytdl-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Mon Jun 22 2020 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.5.5-1
- Update to version 0.5.5

* Thu Jul 18 2019 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.5.4-2
- Disabled building of python2 package for Fedora 30+

* Sat Feb 24 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.5.4-1
- Update to version 0.5.4.
- For python2 backend switched to 'internal'

* Fri Feb 17 2017 root - 0.5.3.1-1
- Initial package.
