# TODO:
# - python-PyKDE4 whatever for printer-applet
#
%define		_state		unstable
%define		orgname		kdeutils
%define		qtver		4.6.0
%define		snap		svn1035674

Summary:	K Desktop Environment - utilities
Summary(es.UTF-8):	KDE - Utilitarios
Summary(ja.UTF-8):	KDEデスクトップ環境 - ユーティリティ
Summary(pl.UTF-8):	K Desktop Environment - narzędzia
Summary(pt_BR.UTF-8):	KDE - Utilitários
Summary(ru.UTF-8):	K Desktop Environment - Утилиты
Summary(uk.UTF-8):	K Desktop Environment - Утиліти
Summary(zh_CN.UTF-8):	KDE实用工具
Name:		kde4-kdeutils
Version:	4.3.98
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	8b27bc785c27eda1b09735dd0998ac98
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtAssistant-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtHelp-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	QtXmlPatterns-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gmp-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libarchive-devel
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	libzip-devel
BuildRequires:	net-snmp-devel
BuildRequires:	pkgconfig
BuildRequires:	python-PyKDE4
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	system-config-printer
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE utilities. Package includes:
 - Ark - archive manager,
 - KCalc - calculator KCharSelect,
 - KCharSelect - character Selector,
 - KDEPasswd, password change application
 - KDESsh - SSH frontend,
 - Kdf - disk space GUI,
 - KEdit - text editor,
 - KFloppy - floppy formating tool,
 - KHexEdit - HEX file editor,
 - KJots - note taker,
 - KLaptopDaemon - laptop daemon,
 - KTimer - timer,
 - KTop - task manager,

%description -l es.UTF-8
Utilitarios para KDE. Programas disponibles en este paquete:
 - Ark,
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh,
 - Kdf -
 - KEdit - editor de textos sencillo,
 - KFloppy - herramienta de formatear disquetes,
 - KHexEdit - editor hexadecimal,
 - KJots - bloque de notas,
 - KLaptopDaemon,
 - KTimer.

%description -l ja.UTF-8
KDEデスクトップ環境用のユーティリティ
以下のようなパッケージが入っています。

- ark - アーカイブ操作ツール
- kcalc - 電卓
- kedit - テキストエディタ
- kfloppy - フロッピーフォーマッタ
- kjots - note taker

%description -l pl.UTF-8
Narzędzia dla KDE. Pakiet zawiera:
 - Ark - program do zarządzania archiwami,
 - KCalc - kalkulator,
 - KCharSelect - narzędzie do wybierania znaków,
 - KDEPasswd,
 - KDESsh - narzędzie do zdalnego wykonywania programów,
 - Kdf - graficzny interfejs do sprawdzania miejsca na dysku,
 - KEdit - edytor tekstu,
 - KFloppy - narzędzie do formatowania dyskietek,
 - KJots - notatnik,
 - KLaptopDaemon - demon dla laptopów,
 - KTimer - timer,
 - KTop - zarządca zadań,

%description -l pt_BR.UTF-8
Utilitários para o KDE. Programas disponíveis neste pacote:
 - Ark - controle de tempo pessoal,
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh - ferramenta de execução remota de programas,
 - KEdit - editor de textos simples
 - KFloppy - ferramenta de formatação de disquetes,
 - KJots - bloco de notas,
 - KLaptopDaemon - miniaplicativo de status de bateria para laptops,
 - KTimer - Monitor de tempo em forma de mini-aplicativo.

%description -l ru.UTF-8
Утилиты для K Desktop Environment. Включает:
 - ark - менеджер архивов tar/gzip,
 - kcalc - научный калькулятор,
 - kedit - простой текстовый редактор,
 - kfloppy - утилита для форматирования
   флоппи-дисков,
 - kjots - блокнот,

%description -l uk.UTF-8
Утилиты для K Desktop Environment. Містить:
 - ark - менеджер архівів tar/gzip,
 - kcalc - научний калькулятор,
 - kedit - простий текстовий редактор,
 - kfloppy - утиліта для форматування
   флопі-дисків,
 - kjots - нотатник,

%package devel
Summary:	Header files for compiling applications that use kdeutils libraries
Summary(pl.UTF-8):	Pliki nagłówkowe do kompilacji aplikacji używających bibliotek kdeutils
Summary(pt_BR.UTF-8):	Arquivos de inclusão para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Requires:	kde4-kdebase-devel >= %{version}

%description devel
This package includes the header files you will need to compile
applications that use kdeutils libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do kompilacji
aplikacji używających bibliotek kdeutils.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para desenvolvimento e compilação de programas
que usem as bibliotecas do kdeutils

%package ark
Summary:	KDE Archive Manager
Summary(pl.UTF-8):	Zarządca archiwów dla KDE
Summary(pt_BR.UTF-8):	Gerenciador de pacotes TAR/comprimidos do KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Requires:	libarchive
Requires:	libzip

%description ark
Ark is a program for managing and quickly extracting archives. It
supports arj, rar, zip, tar, zoo, lha and other formats.

%description ark -l pl.UTF-8
Ark jest programem służącym do zarządzania i szybkiego
rozpakowywania archiwów. Obsługuje archiwa arj, rar, zip, tar, zoo,
lha oraz inne formaty.

%description ark -l pt_BR.UTF-8
Gerenciador de pacotes TAR/comprimidos do KDE.

%package okteta
Summary:	Binary file editor
Summary(pl.UTF-8):	Edytor plików binarnych
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description okteta
The program Okteta is another implementation of a standalone, plain
old-fashioned hex editor. It is based on the libkakao framework, with
plugins using the basic Okteta core and gui libraries.

%description okteta -l pl.UTF-8
Okteta to kolejna implementacja samodzielnego, tradycyjnego edytora
szesnastkowego. Jest oparty na szkielecie libkakao z wtyczkami
wykorzystującymi biblioteki core i gui Okteta.

%package kcalc
Summary:	KDE Calculator
Summary(pl.UTF-8):	Kalkulator dla KDE
Summary(pt_BR.UTF-8):	Calculadora do KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kcalc
Calculator for KDE.

%description kcalc -l pl.UTF-8
Kalkulator dla KDE.

%description kcalc -l pt_BR.UTF-8
Calculadora do KDE.

%package kcharselect
Summary:	KDE Character Selector
Summary(pl.UTF-8):	Program do wybierania znaków dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de seleção de caracteres
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kcharselect
Application for selecting characters.

%description kcharselect -l pl.UTF-8
Program do wybierania znaków.

%package kdessh
Summary:	KDE SSH Frontend
Summary(pl.UTF-8):	Frontend SSH dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de execução remota de programas
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}

%description kdessh
A KDE SSH frontend.

%description kdessh -l pl.UTF-8
Frontend SSH dla KDE.

%description kdessh -l pt_BR.UTF-8
Ferramenta de execução remota de programas.

%package kdf
Summary:	KDE Disk space GUI
Summary(pl.UTF-8):	df dla KDE
Summary(pt_BR.UTF-8):	Mostra o status de espaço em disco
Group:		X11/Applications
Requires:	kde4-kdebase-infocenter >= %{version}

%description kdf
This program shows the disk usage of the mounted devices.

%description kdf -l pl.UTF-8
Ten program pokazuje zajętość dysku dla zamontowanych urządzeń.

%description kdf -l pt_BR.UTF-8
Mostra o status de espaço em disco.

%package kedit
Summary:	KDE Text Editor
Summary(pl.UTF-8):	Edytor tekstu dla KDE
Summary(pt_BR.UTF-8):	Editor de texto melhorado do KDE
Group:		X11/Applications/Editors
Requires:	kde4-kdebase >= %{version}

%description kedit
Simple text editor for KDE.

%description kedit -l pl.UTF-8
Prosty edytor tekstu dla KDE.

%description kedit -l pt_BR.UTF-8
Editor de texto melhorado do KDE.

%package kfloppy
Summary:	KDE Floppy Formater
Summary(pl.UTF-8):	Program formatujący dyskietki dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de formatação de disquetes
Group:		X11/Applications
Requires:	dosfstools
Requires:	kde4-kdebase >= %{version}

%description kfloppy
KFloppy formats floppy disks and puts a DOS or ext2fs filesystem on
them.

%description kfloppy -l pl.UTF-8
KFloppy formatuje dyskietki i zakłada na nich system plików DOS lub
ext2.

%description kfloppy -l pt_BR.UTF-8
Ferramenta de formatação de disquetes.

%package kgpg
Summary:	A frontend for gpg
Summary(pl.UTF-8):	Nakładka graficzna na gpg
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kgpg
kgpg is a simple, free, open source KDE frontend for gpg. It features
- editor mode enables you to type/paste a text and
  encrypt/decrypt/sign/verify it
- key manager: import, export, delete, sign, generate and edit keys.
- integration with konqueror: left click on a file to decrypt/verify
  it, right click on a file to encrypt/sign it.
- encryption: support for symetric encryption. Multiple keys & default
  key encryption. Optional shredding of source files
- signatures: creation & verification of detached & cleartext
  signatures
- drag & drop encryption + clipboard en/decryption

%description kgpg -l pl.UTF-8
kgpg jest prostą, darmową, z otwartymi źródłami, graficzną
nakładką na gpg przeznaczoną dla KDE. Ma następujące
możliwości:
- tryb edytora umożliwiający napisanie/wklejenie tekstu oraz
  zaszyfrowanie/odszyfrowanie/podpisanie/sprawdzenie go,
- zarządzanie kluczami: import, eksport, usuwanie, podpisywanie,
  generowanie oraz edycję,
- integrację z Konquerorem: kliknięcie lewym przyciskiem na pliku w
  celu odszyfrowania/sprawdzenia go, kliknięcie prawym przyciskiem na
  pliku w celu zaszyfrowania/podpisania go,
- szyfrowanie: obsługa szyfrów symetrycznych; wiele kluczy i
  domyślne szyfrowanie kluczem; opcjonalnie niszczenie plików
  źródłowych,
- sygnatury: tworzenie i sprawdzanie oddzielonych i czysto tekstowych
  sygnatur,
- szyfrowanie metodą przeciągnij-i-upuść oraz szyfrowanie i
  odszyfrowywanie schowka.

%package kjots
Summary:	KDE Note taker
Summary(pl.UTF-8):	Notatnik dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description kjots -l pl.UTF-8
KJots to mały program do zapisywania notatek.

%description kjots -l pt_BR.UTF-8
Ferramenta de armazenamento de livros.

%package ktimer
Summary:	KDE Timer
Summary(pl.UTF-8):	Timer dla KDE
Summary(pt_BR.UTF-8):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}

%description ktimer
This is a timer application for KDE. It allows you to execute commands
after a certain amount of time. It allows looping commands as well as
delaying the execution of a command.

%description ktimer -l pl.UTF-8
To jest aplikacja timera dla KDE. Umożliwia wykonywanie poleceń po
określonym czasie, zapętlanie poleceń, a także opóźnienie
wykonywania poleceń.

%description ktimer -l pt_BR.UTF-8
Monitor de tempo em forma de mini-aplicativo.

%package kwalletmanager
Summary:	Password management tool for KDE
Summary(pl.UTF-8):	Narzędzie do zarządzania hasłami dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kwalletmanager
Password management tool for KDE.

%description kwalletmanager -l pl.UTF-8
Narzędzie do zarządzania hasłami w KDE.

%package superkaramba
Summary:	Little interactive widgets on KDE desktop
Summary(pl.UTF-8):	Małe interaktywne widżety na pulpicie KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}
Provides:	superkaramba = %{version}-%{release}

%description superkaramba
SuperKaramba is a tool that allows anyone to easily create and run
little interactive widgets on a KDE desktop.

%description superkaramba -l pl.UTF-8
SuperKaramba to narzędzie pozwalające na łatwe tworzenie i
uruchamianie małych interaktywnych widżetów na pulpicie KDE.

%package printer-applet
Summary:	Printer status applet for KDE
Summary(pl.UTF-8):	Aplet stanu drukarki dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description printer-applet
KDE Printer Applet is a system tray utility which shows current print
jobs and printer warnings or errors.

%description printer-applet -l pl.UTF-8
KDE Printer Applet to narzędzie tacki systemowej pokazujące
bieżące zadania drukarki oraz ostrzeżenia i błędy.

%package irkick
Summary:	KDE Irkick
Summary(pl.UTF-8):	Irkick dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description irkick
KDE LIRC is the infrastructure for the KDE's Infrared Remote Control
functionality. IRKick is the server component of that infrastructure.

%description irkick -l pl.UTF-8
irkick.

%package profiles
Summary:	KDE Profiles for Aplications
Summary(pl.UTF-8):	Profile aplikacji dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description profiles
Profiles for aplications.

%description profiles -l pl.UTF-8
Profile do aplikacji.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DINSTALL_PRINTER_APPLET=TRUE \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# unsupported
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/locolor

#%find_lang ark			--with-kde
#%find_lang okteta		--with-kde
#%find_lang kcalc		--with-kde
#%find_lang kcharselect		--with-kde
#%find_lang kdf			--with-kde
#%find_lang kfloppy		--with-kde
#%find_lang kgpg			--with-kde
#%find_lang ktimer		--with-kde
#%find_lang kwallet		--with-kde
#%find_lang superkaramba		--with-kde
#%find_lang ktimer		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	ark		-p /sbin/ldconfig
%postun	ark		-p /sbin/ldconfig

%post	okteta		-p /sbin/ldconfig
%postun	okteta		-p /sbin/ldconfig

%post	superkaramba	-p /sbin/ldconfig
%postun	superkaramba	-p /sbin/ldconfig

%post	irkick	-p /sbin/ldconfig
%postun	irkick	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkerfuffle.so
%attr(755,root,root) %{_libdir}/libsuperkaramba.so
%attr(755,root,root) %{_libdir}/liboktetagui.so
%attr(755,root,root) %{_libdir}/liboktetacore.so
%attr(755,root,root) %{_libdir}/libkdelirc_shared.so
%attr(755,root,root) %{_libdir}/libkastencontrollers.so
%attr(755,root,root) %{_libdir}/libkastencore.so
%attr(755,root,root) %{_libdir}/libkastengui.so
%attr(755,root,root) %{_libdir}/liboktetakastencontrollers.so
%attr(755,root,root) %{_libdir}/liboktetakastencore.so
%attr(755,root,root) %{_libdir}/liboktetakastengui.so

#%{_includedir}/KDE/Kasten
#%{_includedir}/KDE/Okteta
#%{_includedir}/kasten
#%{_includedir}/okteta

%files profiles
%defattr(644,root,root,755)
%{_datadir}/apps/profiles/amarok.profile.xml
%{_datadir}/apps/profiles/dragonplayer.profile.xml
%{_datadir}/apps/profiles/klauncher.profile.xml
%{_datadir}/apps/profiles/kmix.profile.xml
%{_datadir}/apps/profiles/konqueror.profile.xml
#%{_datadir}/apps/profiles/kscd.profile.xml
%{_datadir}/apps/profiles/okular.profile.xml
%{_datadir}/apps/profiles/profile.dtd
%{_datadir}/apps/profiles/shutdown.profile.xml
%{_datadir}/apps/profiles/suspend.profile.xml
%{_datadir}/apps/profiles/vlc.profile.xml

%files ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%attr(755,root,root) %{_libdir}/kde4/arkpart.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libarchive.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libgz.so
%attr(755,root,root) %ghost %{_libdir}/libkerfuffle.so.?
%attr(755,root,root) %{_libdir}/libkerfuffle.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_cli7z.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_clirar.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_clizip.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libbz2.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libxz.so
#%attr(755,root,root) %{_libdir}/kde4/libextracthere.so
%{_datadir}/apps/ark
%{_datadir}/kde4/servicetypes/kerfufflePlugin.desktop
%{_datadir}/kde4/services/ark_part.desktop
%{_datadir}/kde4/services/kerfuffle_libarchive.desktop
%{_datadir}/kde4/services/kerfuffle_libgz.desktop
#%{_datadir}/kde4/services/ark_dndextract.desktop
%{_datadir}/kde4/services/kcm_lirc.desktop
%{_datadir}/kde4/services/kerfuffle_cli7z.desktop
%{_datadir}/kde4/services/kerfuffle_clirar.desktop
%{_datadir}/kde4/services/kerfuffle_clizip.desktop
%{_datadir}/kde4/services/kerfuffle_libbz2.desktop
%{_datadir}/kde4/services/kerfuffle_libxz.desktop
%{_datadir}/kde4/services/ServiceMenus/ark_addtoservicemenu.desktop
%{_datadir}/kde4/services/ServiceMenus/ark_servicemenu.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_desktopdir}/kde4/ark.desktop
%{_kdedocdir}/en/ark
%{_mandir}/man1/ark.1.*
## ?
%attr(755,root,root) %{_bindir}/sweeper
%{_desktopdir}/kde4/sweeper.desktop
%dir %{_datadir}/apps/sweeper
%{_datadir}/apps/sweeper/sweeperui.rc
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml

%files okteta
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okteta
%attr(755,root,root) %{_libdir}/kde4/libkbytearrayedit.so
%attr(755,root,root) %{_libdir}/kde4/oktetapart.so
%attr(755,root,root) %ghost %{_libdir}/liboktetacore.so.?
%attr(755,root,root) %{_libdir}/liboktetacore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboktetagui.so.?
%attr(755,root,root) %{_libdir}/liboktetagui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboktetakastencore.so.?
%attr(755,root,root) %{_libdir}/liboktetakastencore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboktetakastencontrollers.so.?
%attr(755,root,root) %{_libdir}/liboktetakastencontrollers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboktetakastengui.so.?
%attr(755,root,root) %{_libdir}/liboktetakastengui.so.*.*.*
%{_desktopdir}/kde4/okteta.desktop
%dir %{_datadir}/apps/okteta
%{_datadir}/apps/okteta/oktetaui.rc
%dir %{_datadir}/apps/oktetapart
%{_datadir}/apps/oktetapart/oktetapartbrowserui.rc
%{_datadir}/apps/oktetapart/oktetapartreadonlyui.rc
%{_datadir}/apps/oktetapart/oktetapartreadwriteui.rc
%{_iconsdir}/hicolor/*x*/apps/okteta.png
%{_datadir}/kde4/services/kbytearrayedit.desktop
%{_datadir}/kde4/services/oktetapart.desktop
%{_kdedocdir}/en/okteta
#kasten
%attr(755,root,root) %ghost %{_libdir}/libkastencore.so.?
%attr(755,root,root) %{_libdir}/libkastencore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkastencontrollers.so.?
%attr(755,root,root) %{_libdir}/libkastencontrollers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkastengui.so.?
%attr(755,root,root) %{_libdir}/libkastengui.so.*.*.*

%files kcalc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%attr(755,root,root) %{_libdir}/libkdeinit4_kcalc.so
%{_datadir}/apps/kcalc
%{_datadir}/apps/kconf_update/kcalcrc.upd
%{_datadir}/config.kcfg/kcalc.kcfg
%{_desktopdir}/kde4/kcalc.desktop
%{_kdedocdir}/en/kcalc
#%{_iconsdir}/*/*/apps/kcalc.*

%files kcharselect
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_datadir}/apps/kcharselect
%{_datadir}/apps/kconf_update/kcharselect.upd
%{_desktopdir}/kde4/KCharSelect.desktop
%{_kdedocdir}/en/kcharselect

#%files kdessh
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kdessh

%files kdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%attr(755,root,root) %{_libdir}/kde4/kcm_kdf.so
%{_datadir}/kde4/services/kcmdf.desktop
%{_datadir}/apps/kdf
%{_desktopdir}/kde4/kdf.desktop
%{_desktopdir}/kde4/kwikdisk.desktop
%{_iconsdir}/*/*/apps/kcmdf.*
%{_iconsdir}/*/*/apps/kdf.*
%{_iconsdir}/*/*/apps/kwikdisk.*
%{_kdedocdir}/en/kdf

%files kfloppy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
#%{_datadir}/kde4/services/ServiceMenus/floppy_format.desktop
%{_desktopdir}/kde4/KFloppy.desktop
%{_iconsdir}/*/*/apps/kfloppy.*
%{_kdedocdir}/en/kfloppy

%files kgpg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
%{_datadir}/apps/kgpg
%{_datadir}/kde4/services/ServiceMenus/encryptfile.desktop
%{_datadir}/kde4/services/ServiceMenus/encryptfolder.desktop
%{_datadir}/kde4/services/ServiceMenus/viewdecrypted.desktop
%{_datadir}/autostart/kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_desktopdir}/kde4/kgpg.desktop
%{_iconsdir}/*/*/apps/kgpg.*
%{_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml
%{_kdedocdir}/en/kgpg

%files ktimer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_desktopdir}/kde4/ktimer.desktop
%{_iconsdir}/*/*/*/ktimer.png
%{_kdedocdir}/en/ktimer

%files kwalletmanager
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwalletmanager
%attr(755,root,root) %{_libdir}/kde4/kcm_kwallet.so
%{_datadir}/apps/kwalletmanager
%{_datadir}/kde4/services/kwalletmanager_show.desktop
%{_datadir}/kde4/services/kwalletconfig.desktop
%{_desktopdir}/kde4/kwalletmanager.desktop
%{_desktopdir}/kde4/kwalletmanager-kwalletd.desktop
%{_iconsdir}/hicolor/*/apps/kwalletmanager*.png
%{_kdedocdir}/en/kwallet

%files superkaramba
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/superkaramba
%attr(755,root,root) %{_libdir}/libsuperkaramba.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsuperkaramba.so.?
%attr(755,root,root) %{_libdir}/kde4/plasma_package_superkaramba.so
%attr(755,root,root) %{_libdir}/kde4/plasma_scriptengine_superkaramba.so
%{_datadir}/apps/superkaramba
%{_datadir}/config/superkaramba.knsrc
%{_datadir}/dbus-1/interfaces/org.kde.superkaramba.xml
%{_datadir}/kde4/services/plasma-package-superkaramba.desktop
%{_datadir}/kde4/services/plasma-scriptengine-superkaramba.desktop
%{_desktopdir}/kde4/superkaramba.desktop
%{_iconsdir}/[!l]*/*/*/superkaramba*.*
%{_kdedocdir}/en/superkaramba

%files printer-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/printer-applet
%dir %{_datadir}/apps/printer-applet
%{_datadir}/apps/printer-applet/printer-applet-printers.ui
%{_datadir}/apps/printer-applet/printer-applet.py
%{_datadir}/apps/printer-applet/printer-applet.ui
%{_datadir}/apps/printer-applet/printer-appletui.rc
%{_datadir}/apps/printer-applet/authconn.py
%{_datadir}/apps/printer-applet/debug.py
%{_datadir}/apps/printer-applet/monitor.py
%{_datadir}/apps/printer-applet/printer-applet.notifyrc
%{_datadir}/apps/printer-applet/statereason.py
%{_datadir}/autostart/printer-applet.desktop

%files irkick
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/irkick
%attr(755,root,root) %{_libdir}/kde4/kcm_lirc.so
%attr(755,root,root) %{_libdir}/libkdeinit4_irkick.so
%attr(755,root,root) %ghost %{_libdir}/libkdelirc_shared.so.?
%attr(755,root,root) %{_libdir}/libkdelirc_shared.so.1.0.0
%{_desktopdir}/kde4/irkick.desktop
%dir %{_datadir}/apps/irkick
%{_datadir}/apps/irkick/irkick.notifyrc
#%{_datadir}/apps/remotes/AppleRemote.remote.xml
#%{_datadir}/apps/remotes/AsusDH.remote.xml
#%{_datadir}/apps/remotes/RM-0010.remote.xml
#%{_datadir}/apps/remotes/cimr100.remote.xml
#%{_datadir}/apps/remotes/hauppauge.remote.xml
#%{_datadir}/apps/remotes/packbell.remote.xml
#%{_datadir}/apps/remotes/remote.dtd
#%{_datadir}/apps/remotes/sherwood.remote.xml
#%{_datadir}/apps/remotes/sonytv.remote.xml
%{_datadir}/autostart/irkick.desktop
%{_iconsdir}/hicolor/22x22/apps/irkick.png
%{_iconsdir}/oxygen/*x*/devices/infrared-remote.png
%{_iconsdir}/oxygen/*x*/actions/irkickflash.png
%{_iconsdir}/oxygen/*x*/actions/irkickoff.png
%{_kdedocdir}/en/irkick
%{_kdedocdir}/en/kcmlirc
