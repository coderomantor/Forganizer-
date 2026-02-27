[Setup]
AppName=Forganizer
AppVersion=1.0
AppPublisher=Roman Ullah
DefaultDirName={autopf}\Forganizer
DefaultGroupName=Forganizer
OutputDir=C:\Users\RomanUllah\Desktop\Forganizer\Forganizer-\Forganizer_Installer
OutputBaseFilename=Forganizer_Setup
SetupIconFile=C:\Users\RomanUllah\Desktop\Forganizer\Forganizer-\icon.ico
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "C:\Users\RomanUllah\Desktop\Forganizer\Forganizer-\Forganizer_Installer\file_organiser.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\RomanUllah\Desktop\Forganizer\Forganizer-\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\RomanUllah\Desktop\Forganizer\Forganizer-\README.md"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
; Context menu entry for the background of directories
Root: HKCR; Subkey: "Directory\Background\shell\Forganizer"; ValueType: string; ValueName: ""; ValueData: "&Forganizer by Roman"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\Background\shell\Forganizer"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\icon.ico"
Root: HKCR; Subkey: "Directory\Background\shell\Forganizer\command"; ValueType: string; ValueName: ""; ValueData: """{app}\file_organiser.exe"""

; Clean up the old typo'd key if it exists
Root: HKCR; Subkey: "Directory\Background\shell\Forganiser"; Flags: uninsdeletekey dontcreatekey

[Icons]
Name: "{group}\Uninstall Forganizer"; Filename: "{uninstallexe}"
Name: "{group}\README"; Filename: "{app}\README.md"
