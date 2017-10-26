Summary:	setup.rb - a generic installer for Ruby scripts
Summary(pl.UTF-8):	setup.rb - ogólny instalator dla skryptów języka Ruby
Name:		setup.rb
Version:	3.4.1
Release:	6
License:	LGPL v2.1
Group:		Development/Tools
Source0:	http://i.loveruby.net/archive/setup/setup-%{version}.tar.gz
# Source0-md5:	f0759ec72473e5802d9571df4da6642c
Patch0:		rbconfig-deprecation.patch
URL:		http://i.loveruby.net/en/projects/setup/
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setup.rb is a generic installer for Ruby scripts.

%description -l pl.UTF-8
setup.rb to ogólny instalator dla skryptów języka Ruby.

%prep
%setup -q -n setup-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -p setup.rb $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Makefile README.en TODO doc.en NEWS.en Template.README.en Usage_en.txt sample
%lang(ja) %doc README.ja doc.ja NEWS.ja Template.README.ja Usage_ja.txt
%attr(755,root,root) %{_datadir}/%{name}
