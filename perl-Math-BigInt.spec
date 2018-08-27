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
Version:	1.999813
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	36d7ae0fcb56f748093d9203f1a53336
URL:		http://search.cpan.org/dist/Math-BigInt/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Math-Complex >= 1.39
BuildRequires:	perl-Test-Simple >= 0.94
%endif
# special case: if current perl-modules contain older releases, uncomment Requires and comment Conflicts below
#Requires:	perl-Math-BigInt-FastCalc >= 0.27
#Requires:	perl-Math-BigRat >= 0.2602
#Requires:	perl-bignum >= 0.22
Conflicts:	perl-Math-BigInt-FastCalc < 0.27
Conflicts:	perl-Math-BigInt-GMP < 1.37
Conflicts:	perl-Math-BigInt-Pari < 1.16
Conflicts:	perl-Math-BigRat < 0.2602
Conflicts:	perl-bignum < 0.22
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
%doc BUGS CHANGES CREDITS GOALS HISTORY LICENSE NEW README TODO
%{perl_vendorlib}/Math/BigFloat.pm
%{perl_vendorlib}/Math/BigInt.pm
%{perl_vendorlib}/Math/BigInt/Calc.pm
%{perl_vendorlib}/Math/BigInt/CalcEmu.pm
%{perl_vendorlib}/Math/BigInt/Lib.pm
%{_mandir}/man3/Math::BigFloat.3pm*
%{_mandir}/man3/Math::BigInt.3pm*
%{_mandir}/man3/Math::BigInt::Calc.3pm*
%{_mandir}/man3/Math::BigInt::CalcEmu.3pm*
%{_mandir}/man3/Math::BigInt::Lib.3pm*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.txt
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
