%global octpkg doctest

Summary:	Documentation tests for Octave
Name:		octave-doctest
Version:	0.8.0
Release:	1
License:	BSD
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/doctest/
Url:		https://github.com/gnu-octave/octave-doctest/
Source0:	https://github.com/gnu-octave/octave-doctest/releases/download/v%{version}/doctest-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
The Octave-Forge Doctest package finds specially-formatted
blocks of example code within documentation files.  It then executes
the code and confirms the output is correct.  This can be useful as part of
a testing framework or simply to ensure that documentation stays up-to-date
during software development.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

