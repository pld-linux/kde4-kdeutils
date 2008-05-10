#
%define		_state		unstable
%define		orgname		kdeutils
Summary:	K Desktop Environment - utilities
Summary(es.UTF-8):	KDE - Utilitarios
Summary(ja.UTF-8):	KDEデスクトップ環境 - ユーティリティ
Summary(pl.UTF-8):	K Desktop Environment - narzędzia
Summary(pt_BR.UTF-8):	KDE - Utilitários
Summary(ru.UTF-8):	K Desktop Environment - Утилиты
Summary(uk.UTF-8):	K Desktop Environment - Утиліти
Summary(zh_CN.UTF-8):	KDE实用工具
Name:		kde4-kdeutils
Version:	4.0.73
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	7a4c055b5f48dfe190b92755e1b9df07
URL:		http://www.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ed
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gmp-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	libarchive-devel
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	libzip-devel
BuildRequires:	net-snmp-devel
%ifarch %{ix86} ppc
BuildRequires:	pbbuttonsd-lib >= 0.6.8
%endif
BuildRequires:	net-snmp-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-modules
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake >= 040511
%{?with_xmms:BuildRequires:	xmms-devel}
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
 - ksim - system monitor.

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
 - ksim

%description -l ja.UTF-8
KDEデスクトップ環境用のユーティリティ 以下のようなパッケージが入っています。

- ark - アーカイブ操作ツール
- kcalc - 電卓
- kedit - テキストエディタ
- kfloppy - フロッピーフォーマッタ
- khexedit - バイナリエディタ
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
 - KHexedit - szesnastkowy edytor plików,
 - KJots - notatnik,
 - KLaptopDaemon - demon dla laptopów,
 - KTimer - timer,
 - KTop - zarządca zadań,
 - ksim - monitor systemu.

%description -l pt_BR.UTF-8
Utilitários para o KDE. Programas disponíveis neste pacote:
 - Ark - controle de tempo pessoal,
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh - ferramenta de execução remota de programas,
 - KEdit - editor de textos simples
 - KFloppy - ferramenta de formatação de disquetes,
 - KHexEdit - editor hexadecimal,
 - KJots - bloco de notas,
 - KLaptopDaemon - miniaplicativo de status de bateria para laptops,
 - KTimer - Monitor de tempo em forma de mini-aplicativo.

%description -l ru.UTF-8
Утилиты для K Desktop Environment. Включает:
 - ark - менеджер архивов tar/gzip,
 - kcalc - научный калькулятор,
 - kedit - простой текстовый редактор,
 - kfloppy - утилита для форматирования флоппи-дисков,
 - khexedit - редактор бинарных файлов,
 - kjots - блокнот,

%description -l uk.UTF-8
Утилиты для K Desktop Environment. Містить:
 - ark - менеджер архівів tar/gzip,
 - kcalc - научний калькулятор,
 - kedit - простий текстовий редактор,
 - kfloppy - утиліта для форматування флопі-дисків,
 - khexedit - редактор бінарних файлів,
 - kjots - нотатник,

%package devel
Summary:	Header files for compiling applications that use kdeutils libraries
Summary(pl.UTF-8):	Pliki nagłówkowe do kompilacji aplikacji używających bibliotek kdeutils
Summary(pt_BR.UTF-8):	Arquivos de inclusão para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Requires:	%{name}-klaptopdaemon = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Requires:	%{name}-kregexpeditor = %{epoch}:%{version}-%{release}
Requires:	%{name}-ksim = %{epoch}:%{version}-%{release}
Requires:	kde4-kdebase-devel >= %{version}

%description devel
This package includes the header files you will need to compile
applications that use kdeutils libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do kompilacji aplikacji
używających bibliotek kdeutils.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para desenvolvimento e compilação de programas
que usem as bibliotecas do kdeutils

%package ark
Summary:	KDE Archive Manager
Summary(pl.UTF-8):	Zarządca archiwów dla KDE
Summary(pt_BR.UTF-8):	Gerenciador de pacotes TAR/comprimidos do KDE
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}
Requires:	libarchive
Requires:	libzip

%description ark
Ark is a program for managing and quickly extracting archives. It
supports arj, rar, zip, tar, zoo, lha and other formats.

%description ark -l pl.UTF-8
Ark jest programem służącym do zarządzania i szybkiego rozpakowywania
archiwów. Obsługuje archiwa arj, rar, zip, tar, zoo, lha oraz inne
formaty.

%description ark -l pt_BR.UTF-8
Gerenciador de pacotes TAR/comprimidos do KDE.

%package okteta
Summary:	Binary file editor
Summary(pl.UTF-8):	Edytor plików binarnych
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}

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
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kcalc

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
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kcharselect

%description kcharselect
Application for selecting characters.

%description kcharselect -l pl.UTF-8
Program do wybierania znaków.

%package kdelirc
Summary:	KDE frontend for the Linux Infrared Remote Control system
Summary(pl.UTF-8):	Frontend KDE dla systemu LIRC (zdalnego sterowania podczerwienią)
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}

%description kdelirc
KDELIRC is a KDE frontend for the Linux Infrared Remote Control
system. It has two aims:
- provide a control center module for configuration of application
  bindings to remote control buttons and actual remote controls
  installed (i.e. lirc configuration).
- provide a system-tray applet to act as a proxy between the LIRC
  system and KDE (applications).

%description kdelirc -l pl.UTF-8
KDELIRC to frontend KDE dla systemu LIRC (Linux Infrared Remote
Control - zdalnego sterowania podczerwienią). Ma dwa cele:
- zapewnienie modułu dla centrum sterowania do konfiguracji dowiązań
  aplikacji do przycisków pilota oraz konfiguracji samych pilotów (czyli
  konfiguracji lirc)
- zapewnienie apletu tacki systemowej służącego jako proxy pomiędzy
  systemem LIRC oraz KDE (aplikacjami).

%package kdessh
Summary:	KDE SSH Frontend
Summary(pl.UTF-8):	Frontend SSH dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de execução remota de programas
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdessh

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
Obsoletes:	kdf

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
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kedit

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
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kfloppy

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
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kgpg

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
kgpg jest prostą, darmową, z otwartymi źródłami, graficzną nakładką na
gpg przeznaczoną dla KDE. Ma następujące możliwości:
- tryb edytora umożliwiający napisanie/wklejenie tekstu oraz
  zaszyfrowanie/odszyfrowanie/podpisanie/sprawdzenie go,
- zarządzanie kluczami: import, eksport, usuwanie, podpisywanie,
  generowanie oraz edycję,
- integrację z Konquerorem: kliknięcie lewym przyciskiem na pliku w
  celu odszyfrowania/sprawdzenia go, kliknięcie prawym przyciskiem na
  pliku w celu zaszyfrowania/podpisania go,
- szyfrowanie: obsługa szyfrów symetrycznych; wiele kluczy i domyślne
  szyfrowanie kluczem; opcjonalnie niszczenie plików źródłowych,
- sygnatury: tworzenie i sprawdzanie oddzielonych i czysto tekstowych
  sygnatur,
- szyfrowanie metodą przeciągnij-i-upuść oraz szyfrowanie i
  odszyfrowywanie schowka.

%package khexedit
Summary:	KDE Hex Editor
Summary(pl.UTF-8):	Edytor szesnastkowy dla KDE
Summary(pt_BR.UTF-8):	Editor hexadecimal para arquivos binários
Group:		X11/Applications/Editors
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	khexedit

%description khexedit
Hex Editor is a small and simple viewer for binary files.

%description khexedit -l pl.UTF-8
Hex Editor jest małym i prostym edytorem plików binarnych.

%description khexedit -l pt_BR.UTF-8
Editor hexadecimal para arquivos binários.

%package kjots
Summary:	KDE Note taker
Summary(pl.UTF-8):	Notatnik dla KDE
Summary(pt_BR.UTF-8):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kjots

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description kjots -l pl.UTF-8
KJots to mały program do zapisywania notatek.

%description kjots -l pt_BR.UTF-8
Ferramenta de armazenamento de livros.

%package klaptopdaemon
Summary:	KDE Laptop Daemon
Summary(pl.UTF-8):	Wskaźnik zużycia baterii w laptopie dla KDE
Summary(pt_BR.UTF-8):	Miniaplicativo de status de bateria para laptops
Group:		X11/Applications
Requires:	kde4-kdebase-infocenter >= %{version}
%ifarch %{ix86}
Requires:	tpctl
%endif
Obsoletes:	laptop

%description klaptopdaemon
A laptop battery monitoring tool for KDE

%description klaptopdaemon -l pl.UTF-8
Wskaźnik zużycia baterii w laptopie dla KDE.

%description klaptopdaemon -l pt_BR.UTF-8
Miniaplicativo de status de bateria para laptops

%package kmilo
Summary:	KDE support for various types of hardware input devices
Summary(pl.UTF-8):	Wsparcie KDE dla różnych rodzajów sprzętowych urządzeń wejściowych
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kdeutils-kmilo-kvaio
Obsoletes:	kdeutils-kmilo-powerbook

%description kmilo
This is a kded module that can be extended to support various types of
hardware input devices that exist, such as those on keyboards. It
presently supports:
- PowerBooks
- Sony Vaio laptops (tested on Vaio PCG-GRX series)

%description kmilo -l pl.UTF-8
To jest moduł kded, który może być rozszerzany, by obsługiwać różne
rodzaje sprzętowych urządzeń wejściowych, takich jak te na
klawiaturze. Aktualnie obsługuje:
- PowerBooki
- laptopy Sony Vaio (testowany na Vaio z serii PCG-GRX)

%package kmilo-kvaio
Summary:	Sony Vaio KMilo module
Summary(pl.UTF-8):	Moduł KMilo dla laptopów Sony Vaio
Group:		X11/Applications
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kdeutils-kmilo

%description kmilo-kvaio
KMilo module for Sony Vaio laptop support.

%description kmilo-kvaio -l pl.UTF-8
Moduł KMilo dla laptopów Sony Vaio.

%package kmilo-powerbook
Summary:	PowerBook KMilo module
Summary(pl.UTF-8):	Moduł KMilo dla PowerBooków
Group:		X11/Applications
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kdeutils-kmilo

%description kmilo-powerbook
KMilo module for PowerBooks support.

%description kmilo-powerbook -l pl.UTF-8
Moduł KMilo dla PowerBooków.

%package kmilo-thinkpad
Summary:	ThinkPad KMilo module
Summary(pl.UTF-8):	Moduł KMilo dla ThinkPadów
Group:		X11/Applications
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Requires:	kde4-kdebase-core >= %{version}

%description kmilo-thinkpad
KMilo module for ThinkPads support.

%description kmilo-thinkpad -l pl.UTF-8
Moduł KMilo dla ThinkPadów.

%package kregexpeditor
Summary:	Graphical regular expression editor
Summary(pl.UTF-8):	Graficzny edytor wyrażeń regularnych
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}
Obsoletes:	kregexpeditor

%description kregexpeditor
Graphical regular expression editor.

%description kregexpeditor -l pl.UTF-8
Graficzny edytor wyrażeń regularnych.

%package ksim
Summary:	K System Information Monitor
Summary(pl.UTF-8):	K System Information Monitor - monitor informacji o systemie
Group:		X11/Applications
Requires:	kde4-kdebase-desktop >= %{version}

%description ksim
A KDE system monitoring tool that features:
- GKrellm theme support
- host name display
- uptime, memory and swap display
- filesystem usage plugin
- disk information plugin
- net plugin being able to monitor eth0, ppp0 and others
- sensor plugin able to monitor any sensor via lm_sensors
- APM laptop battery meter
- CPU plugin that can monitor CPU usage.

%description ksim -l pl.UTF-8
Narzędzie do monitorowania systemu dla KDE o następujących
możliwościach:
- obsługa motywów GKrellma
- wyświetlanie nazwy komputera
- wyświetlanie uptime'u, stanu pamięci i swapa
- wtyczka wykorzystania systemu plików
- wtyczka informacji o dysku
- wtyczka sieciowa potrafiąca monitorować eth0, ppp0 i inne
- wtyczka czujników potrafiąca monitorować dowolne czujniki przez
  lm_sensors
- miernik baterii laptopów korzystający z APM
- wtyczka procesora monitorująca obciążenie procesora.

%package ktimer
Summary:	KDE Timer
Summary(pl.UTF-8):	Timer dla KDE
Summary(pt_BR.UTF-8):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	ktimer

%description ktimer
This is a timer application for KDE. It allows you to execute commands
after a certain amount of time. It allows looping commands as well as
delaying the execution of a command.

%description ktimer -l pl.UTF-8
To jest aplikacja timera dla KDE. Umożliwia wykonywanie poleceń po
określonym czasie, zapętlanie poleceń, a także opóźnienie wykonywania
poleceń.

%description ktimer -l pt_BR.UTF-8
Monitor de tempo em forma de mini-aplicativo.

%package kwalletmanager
Summary:	Password management tool for KDE
Summary(pl.UTF-8):	Narzędzie do zarządzania hasłami dla KDE
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}

%description kwalletmanager
Password management tool for KDE.

%description kwalletmanager -l pl.UTF-8
Narzędzie do zarządzania hasłami w KDE.

%package superkaramba
Summary:	Little interactive widgets on KDE desktop
Summary(pl.UTF-8):	Małe interaktywne widżety na pulpicie KDE
Group:		X11/Applications
Requires:	kde4-kdebase-core >= %{version}
Provides:	superkaramba = %{version}-%{release}
Obsoletes:	superkaramba

%description superkaramba
SuperKaramba is a tool that allows anyone to easily create and run
little interactive widgets on a KDE desktop.

%description superkaramba -l pl.UTF-8
SuperKaramba to narzędzie pozwalające na łatwe tworzenie i
uruchamianie małych interaktywnych widżetów na pulpicie KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
		../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# unsupported
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/locolor

%find_lang ark			--with-kde
%find_lang okteta		--with-kde
#%find_lang irkick		--with-kde
#%find_lang KRegExpEditor	--with-kde
%find_lang kcalc		--with-kde
%find_lang kcharselect		--with-kde
#%find_lang kcontrol		--with-kde
%find_lang kdf			--with-kde
#%find_lang blockdevices		--with-kde
#cat blockdevices.lang >> kdf.lang
#%find_lang kcmlirc		--with-kde
#cat kcmlirc.lang >> irkick.lang
#%find_lang kedit		--with-kde
%find_lang kfloppy		--with-kde
%find_lang kgpg			--with-kde
#%find_lang khexedit		--with-kde
%find_lang kjots		--with-kde
#%find_lang ksim			--with-kde
%find_lang ktimer		--with-kde
%find_lang kwallet		--with-kde
%find_lang superkaramba		--with-kde
%find_lang ktimer		--with-kde

# Omit bogus apidocs entries.
# Otherwise 'kdeutils-apidocs` owner is needed

%clean
rm -rf $RPM_BUILD_ROOT

%post	ark		-p /sbin/ldconfig
%postun	ark		-p /sbin/ldconfig

%post	khexedit	-p /sbin/ldconfig
%postun	khexedit	-p /sbin/ldconfig

%post	klaptopdaemon	-p /sbin/ldconfig
%postun	klaptopdaemon	-p /sbin/ldconfig

%post	kmilo		-p /sbin/ldconfig
%postun	kmilo		-p /sbin/ldconfig

%post	kregexpeditor	-p /sbin/ldconfig
%postun	kregexpeditor	-p /sbin/ldconfig

%post	ksim		-p /sbin/ldconfig
%postun	ksim		-p /sbin/ldconfig

%post	okteta		-p /sbin/ldconfig
%postun	okteta		-p /sbin/ldconfig

%post	superkaramba	-p /sbin/ldconfig
%postun	superkaramba	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkerfuffle.so
%attr(755,root,root) %{_libdir}/libkmilo.so
%attr(755,root,root) %{_libdir}/libsuperkaramba.so
%attr(755,root,root) %{_libdir}/liboktetagui.so
%attr(755,root,root) %{_libdir}/liboktetacore.so

%files ark -f ark.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%attr(755,root,root) %{_libdir}/kde4/libarkpart.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_bk.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libarchive.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libzip.so
%attr(755,root,root) %ghost %{_libdir}/libkerfuffle.so.?
%attr(755,root,root) %{_libdir}/libkerfuffle.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_rar.so
%{_datadir}/apps/ark
%{_datadir}/kde4/servicetypes/kerfufflePlugin.desktop
%{_datadir}/kde4/services/ark_part.desktop
%{_datadir}/kde4/services/kerfuffle_bk.desktop
%{_datadir}/kde4/services/kerfuffle_libarchive.desktop
%{_datadir}/kde4/services/kerfuffle_libzip.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_desktopdir}/kde4/ark.desktop
%{_datadir}/kde4/services/kerfuffle_rar.desktop
## ?
%attr(755,root,root) %{_bindir}/sweeper
%{_desktopdir}/kde4/sweeper.desktop
%{_datadir}/apps/sweeper/sweeperui.rc
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml

%files okteta -f okteta.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okteta
%attr(755,root,root) %{_libdir}/kde4/libarkpart.so
%attr(755,root,root) %{_libdir}/kde4/libkbytearrayedit.so
%attr(755,root,root) %{_libdir}/kde4/liboktetapart.so
%attr(755,root,root) %ghost %{_libdir}/liboktetacore.so.?
%attr(755,root,root) %{_libdir}/liboktetacore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboktetagui.so.?
%attr(755,root,root) %{_libdir}/liboktetagui.so.*.*.*
%{_desktopdir}/kde4/okteta.desktop
%dir %{_datadir}/apps/okteta
%{_datadir}/apps/okteta/oktetaui.rc
%dir %{_datadir}/apps/oktetapart
%{_datadir}/apps/oktetapart/oktetapartui.rc
%{_iconsdir}/hicolor/*x*/apps/okteta.png
%{_datadir}/kde4/services/kbytearrayedit.desktop
%{_datadir}/kde4/services/oktetapart.desktop

%files kcalc -f kcalc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%attr(755,root,root) %{_libdir}/libkdeinit4_kcalc.so
%{_datadir}/apps/kcalc
%{_datadir}/apps/kconf_update/kcalcrc.upd
%{_datadir}/config.kcfg/kcalc.kcfg
%{_desktopdir}/kde4/kcalc.desktop
%{_iconsdir}/*/*/apps/kcalc.*

%files kcharselect -f kcharselect.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_datadir}/apps/kcharselect
%{_datadir}/apps/kconf_update/kcharselect.upd
%{_desktopdir}/kde4/KCharSelect.desktop

#%files kdelirc
#-f irkick.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/irkick
#%attr(755,root,root) %{_libdir}/libkdeinit_irkick.so
#%attr(755,root,root) %{_libdir}/kde4/irkick.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kcmlirc.so
#%{_datadir}/apps/irkick
#%{_datadir}/apps/profiles/klauncher.profile.xml
#%{_datadir}/apps/profiles/konqueror.profile.xml
#%{_datadir}/apps/profiles/noatun.profile.xml
#%{_datadir}/apps/profiles/profile.dtd
#%{_datadir}/apps/remotes/RM-0010.remote.xml
#%{_datadir}/apps/remotes/cimr100.remote.xml
#%{_datadir}/apps/remotes/hauppauge.remote.xml
#%{_datadir}/apps/remotes/remote.dtd
#%{_datadir}/apps/remotes/sherwood.remote.xml
#%{_datadir}/apps/remotes/sonytv.remote.xml
#%{_datadir}/autostart/irkick.desktop
#%{_desktopdir}/kde/irkick.desktop
#%{_desktopdir}/kde/kcmlirc.desktop
#%{_iconsdir}/hicolor/*/apps/irkick.png

%files kdessh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdessh

%files kdf -f kdf.lang
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

#%files kedit
#-f kedit.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kedit
#%attr(755,root,root) %{_libdir}/libkdeinit_kedit.so
#%attr(755,root,root) %{_libdir}/kde4/kedit.so
#%{_datadir}/apps/kedit
#%{_datadir}/config.kcfg/kedit.kcfg
#%{_desktopdir}/kde/KEdit.desktop
#%{_iconsdir}/*/*/apps/kedit.*

%files kfloppy -f kfloppy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_datadir}/kde4/services/ServiceMenus/floppy_format.desktop
%{_desktopdir}/kde4/KFloppy.desktop
%{_iconsdir}/*/*/apps/kfloppy.*

%files kgpg -f kgpg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
%{_datadir}/apps/kgpg
%{_datadir}/kde4/services/ServiceMenus/encryptfile.desktop
%{_datadir}/kde4/services/ServiceMenus/encryptfolder.desktop
%{_datadir}/autostart/kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_desktopdir}/kde4/kgpg.desktop
%{_iconsdir}/*/*/apps/kgpg.*
%{_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml

#%files khexedit
#-f khexedit.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/khexedit
#%attr(755,root,root) %{_libdir}/kde4/libkbyteseditwidget.so
#%attr(755,root,root) %{_libdir}/kde4/libkhexedit2part.so
#%attr(755,root,root) %{_libdir}/libkhexeditcommon.so.*.*.*
#%{_datadir}/apps/khexedit
#%{_datadir}/apps/khexedit2part
#%{_datadir}/services/khexedit2part.desktop
#%{_datadir}/services/kbyteseditwidget.desktop
#%{_desktopdir}/kde/khexedit.desktop
#%{_iconsdir}/*/*/apps/khexedit.*

%files kjots -f kjots.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_datadir}/apps/kjots
%{_datadir}/config.kcfg/kjots.kcfg
%{_desktopdir}/kde4/Kjots.desktop
%{_iconsdir}/*/*/apps/kjots.*

%files kmilo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmilo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmilo.so.?
%attr(755,root,root) %{_libdir}/kde4/kcm_kvaio.so
%attr(755,root,root) %{_libdir}/kde4/kded_kmilod.so
%attr(755,root,root) %{_libdir}/kde4/kmilo_asus.so
%attr(755,root,root) %{_libdir}/kde4/kmilo_delli8k.so
%attr(755,root,root) %{_libdir}/kde4/kmilo_kvaio.so
%{_datadir}/kde4/servicetypes/kmilo/kmilopluginsvc.desktop
%{_datadir}/kde4/services/kded/kmilod.desktop
%{_datadir}/kde4/services/kmilo/kmilo_asus.desktop
%{_datadir}/kde4/services/kmilo/kmilo_delli8k.desktop
%{_datadir}/kde4/services/kmilo/kmilo_kvaio.desktop
%{_datadir}/kde4/services/kvaio.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kmilod.xml

%files kmilo-thinkpad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_thinkpad.so
%attr(755,root,root) %{_libdir}/kde4/kmilo_thinkpad.so
%{_datadir}/kde4/services/kmilo/kmilo_thinkpad.desktop
%{_datadir}/kde4/services/thinkpad.desktop

#%files klaptopdaemon
#-f kcontrol.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/klaptop*
#%attr(755,root,root) %{_libdir}/libkcmlaptop.so.*.*.*
#%attr(755,root,root) %{_libdir}/kde4/kded_klaptopdaemon.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_laptop.so
#%{_datadir}/apps/klaptopdaemon
#%{_datadir}/services/kded/klaptopdaemon.desktop
#%{_desktopdir}/kde/laptop.desktop
#%{_desktopdir}/kde/pcmcia.desktop
#%{_iconsdir}/*/*/*/*laptop*

#%files kregexpeditor
#-f KRegExpEditor.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kregexpeditor
#%attr(755,root,root) %{_libdir}/libkregexpeditorcommon.so.*.*.*
#%attr(755,root,root) %{_libdir}/kde4/libkregexpeditorgui.so
#%{_datadir}/apps/kregexpeditor
#%{_datadir}/services/kregexpeditorgui.desktop
#%{_desktopdir}/kde/kregexpeditor.desktop
#%{_iconsdir}/*/*/*/kregexpeditor.png

#%files ksim
#-f ksim.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libksimcore.so.*.*.*
#%attr(755,root,root) %{_libdir}/kde4/ksim*.so
#%{_datadir}/apps/kicker/extensions/ksim.desktop
#%{_datadir}/apps/ksim
#%{_datadir}/config/ksim_panelextensionrc
#%{_desktopdir}/kde/ksim.desktop
#%{_iconsdir}/*/*/apps/ksim*.png
#%{_iconsdir}/*/*/devices/ksim*.png

%files ktimer -f ktimer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_desktopdir}/kde4/ktimer.desktop
%{_iconsdir}/*/*/*/ktimer.png

%files kwalletmanager -f kwallet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwalletmanager
%attr(755,root,root) %{_libdir}/kde4/kcm_kwallet.so
%{_datadir}/apps/kwalletmanager
%{_datadir}/kde4/services/kwalletmanager_show.desktop
%{_datadir}/kde4/services/kwalletconfig.desktop
%{_desktopdir}/kde4/kwalletmanager.desktop
%{_desktopdir}/kde4/kwalletmanager-kwalletd.desktop
%{_iconsdir}/[!l]*/*/*/kwalletmanager*.*

%files superkaramba -f superkaramba.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/superkaramba
%attr(755,root,root) %{_libdir}/libsuperkaramba.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsuperkaramba.so.?
%attr(755,root,root) %{_libdir}/kde4/plasma_package_superkaramba.so
%attr(755,root,root) %{_libdir}/kde4/plasma_scriptengine_superkaramba.so
%{_datadir}/apps/superkaramba
%{_desktopdir}/kde4/superkaramba.desktop
%{_iconsdir}/[!l]*/*/*/superkaramba*.*
%{_datadir}/kde4/services/plasma-scriptengine-superkaramba.desktop
%{_datadir}/kde4/services/plasma-package-superkaramba.desktop
%{_datadir}/config/superkaramba.knsrc
%{_datadir}/dbus-1/interfaces/org.kde.superkaramba.xml
