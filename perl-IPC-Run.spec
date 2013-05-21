%define upstream_name	 IPC-Run
%define upstream_version 0.91

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes
chmod 755 eg/*
perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' eg/*

rm -f lib/IPC/Run/Win32Helper.pm \
      lib/IPC/Run/Win32IO.pm \
      lib/IPC/Run/Win32Pump.pm

sed -i -e '/Win32Helper.pm/d;/Win32IO.pm/d;/Win32Pump.pm/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes TODO eg
%{perl_vendorlib}/IPC
%{_mandir}/*/*


%changelog
* Fri Jul 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.910.0-1
+ Revision: 810450
- Update to 0.91
- Get rid of perl(Win32) dependency

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.900.0-3
+ Revision: 765379
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.900.0-2
+ Revision: 763896
- rebuilt for perl-5.14.x

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1
+ Revision: 688749
- update to new version 0.90

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.890.0-2
+ Revision: 667216
- mass rebuild

* Thu Apr 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.890.0-1mdv2011.0
+ Revision: 530664
- update to 0.89

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-1mdv2010.1
+ Revision: 530265
- update to 0.88

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 0.870.0-1mdv2010.1
+ Revision: 529781
- update to 0.87

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.1
+ Revision: 527734
- update to 0.86

* Tue Mar 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.850.0-1mdv2010.1
+ Revision: 526815
- update to 0.85

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.840.0-1mdv2010.0
+ Revision: 402562
- update to 0.56

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2010.0
+ Revision: 396221
- update to new version 0.84

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-1mdv2010.0
+ Revision: 394084
- update to new version 0.83

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.82-1mdv2010.0
+ Revision: 372503
- update to 0.82

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.80-3mdv2009.1
+ Revision: 351919
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.80-2mdv2009.0
+ Revision: 223803
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

