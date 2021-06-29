%define modname	IPC-Run
%define modver 20200505.0

# Avoid nasty build dependency loop
%define dont_gprintify 1

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/IPC::Run
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/IPC-Run-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
%autosetup -p1 -n %{modname}-%{modver}
chmod 755 eg/*
perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' eg/*

rm -f lib/IPC/Run/Win32Helper.pm \
      lib/IPC/Run/Win32IO.pm \
      lib/IPC/Run/Win32Pump.pm

sed -i -e '/Win32Helper.pm/d;/Win32IO.pm/d;/Win32Pump.pm/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc eg
%{perl_vendorlib}/IPC
%{_mandir}/man3/*
