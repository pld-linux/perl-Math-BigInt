#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInt
Summary:	New versions of Math::BigInt and Math::BigFloat Perl modules
Summary(pl.UTF-8):	Nowe wersje modułów Perla Math::BigInt i Math::BigFloat
Name:		perl-Math-BigInt
Version:	1.87
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	639a8a21dd08ce331ba7e2e4773e59c9
URL:		http://search.cpan.org/dist/Math-BigInt/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#Conflicts:	perl-Math-BigRat < 0.19
#Conflicts:	perl-bignum < 0.21
#...but these are in perl-modules, so we must override them by separate packages:
Requires:	perl-Math-BigRat >= 0.19
Requires:	perl-bignum >= 0.21
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
New versions of Math::BigInt and Math::BigFloat.

%description -l pl.UTF-8
Nowe wersje modułów Math::BigInt i Math::BigFloat.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test INST_ARCHLIB=t}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BENCHMARK BUGS CHANGES CREDITS GOALS HISTORY LICENSE NEW README TODO
%{perl_vendorlib}/Math/*.pm
%{perl_vendorlib}/Math/BigInt/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.txt
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
