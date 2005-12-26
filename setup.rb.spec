Summary:	setup.rb - a generic installer for Ruby scripts
Summary(pl):	setup.rb - og�lny instalator dla skrypt�w j�zyka Ruby
Name:		setup.rb
Version:	3.3.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://i.loveruby.net/archive/setup/setup-%{version}.tar.gz
# Source0-md5:	5df5b2c9e2e575edc17e57d3f859e7b2
URL:		http://i.loveruby.net/en/prog/setup.html
BuildRequires:	rpmbuild(macros) >= 1.272
BuildRequires:	ruby
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setup.rb is a generic installer for Ruby scripts.

%description -l pl
setup.rb to og�lny instalator dla skrypt�w j�zyka Ruby.

%prep
%setup -q -n setup-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

install setup.rb $RPM_BUILD_ROOT%{_datadir}/setup.rb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Makefile README.en TODO doc.en NEWS.en Template.README.en
%doc Usage_en.txt sample
%lang(jp) %doc README.ja doc.ja NEWS.ja Template.README.ja Usage_ja.txt
%attr(755,root,root) %{_datadir}/%{name}
