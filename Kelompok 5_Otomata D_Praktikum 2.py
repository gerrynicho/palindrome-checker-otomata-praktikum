"""
PRAKTIKUM OTOMATA - PALINDROME CHECKER
Input: (letter + digit)* - kombinasi huruf dan angka
Oleh : Kelompok 5 Otomata D
"""

def is_valid_char(char):
    """
    Fungsi untuk memvalidasi karakter input
    
    Args:
        char (str): Karakter yang akan divalidasi
        
    Returns:
        bool: True jika karakter adalah huruf atau angka, False jika tidak
        
    Penjelasan:
        Fungsi ini menggunakan method isalnum() bawaan Python untuk mengecek
        apakah karakter merupakan alphanumeric (huruf atau angka).
        Sesuai dengan grammar (letter + digit)*
    """
    return char.isalnum()

def validate_input(input_string):
    """
    Fungsi untuk memvalidasi seluruh string input
    
    Args:
        input_string (str): String yang akan divalidasi
        
    Returns:
        tuple: (bool, str) - (status validasi, pesan error jika ada)
        
    Penjelasan:
        Fungsi ini melakukan validasi komprehensif:
        1. Mengecek apakah string kosong
        2. Mengecek apakah semua karakter valid (alphanumeric)
        3. Mengembalikan tuple untuk error handling yang lebih baik
    """
    # validator
    if not input_string or input_string.isspace():
        return False, "input jangan kosong dan space only!"
    
    for i, char in enumerate(input_string):
        if not is_valid_char(char):
            return False, f"char'{char}' pada  {i+1} tidak valid! hanya huruf dan angka."
    
    return True, "input valid"

def is_palindrome_with_visualization(input_string):
    """
    fungsi untuk mengecek palindrome dengan visualisasi step-by-step
    
    Args:
        input_string (str): String yang akan dicek
        
    Returns:
        bool: True jika palindrome, False jika tidak
        
    Penjelasan:
        Fungsi ini menggunakan algoritma two-pointer:
        1. Pointer kiri dimulai dari index 0
        2. Pointer kanan dimulai dari index terakhir
        3. Kedua pointer bergerak ke tengah sambil membandingkan karakter
        4. Jika ada yang tidak sama, langsung return False
        5. Visualisasi menunjukkan proses perbandingan setiap step
    """
    length = len(input_string)
    left = 0
    right = length - 1
    step = 1
    
    print(f"\n=== VISUALISASI PENGECEKAN PALINDROME ===")
    print(f"String: '{input_string}' (panjang: {length})")
    print(f"Posisi: {' '.join([f'{i:2d}' for i in range(length)])}")
    print(f"Karakter: {' '.join([f' {c}' for c in input_string])}")
    print("\n---------------------------------------------------------------")
    
    while left < right:
        left_char = input_string[left]
        right_char = input_string[right]
        visual = [' '] * length
        visual[left] = '↑'
        visual[right] = '↑'
        
        print(f"Step {step}: Membandingkan posisi {left} ('{left_char}') dengan posisi {right} ('{right_char}')")
        print(f"         {' '.join([f' {v}' for v in visual])}")
        
        if left_char != right_char:
            print(f"         ❌ '{left_char}' ≠ '{right_char}' → BUKAN PALINDROME")
            return False
        else:
            print(f"         ✅ '{left_char}' = '{right_char}' → Lanjut")
        
        left += 1
        right -= 1
        step += 1
        print()
    
    print("PALINDROME!")
    return True

def is_palindrome_simple(input_string):
    """
    Fungsi palindrome sederhana tanpa visualisasi
    
    Args:
        input_string (str): String yang akan dicek
        
    Returns:
        bool: True jika palindrome, False jika tidak
        
    Penjelasan:
        Implementasi sederhana menggunakan slicing Python.
        input_string[::-1] membalik string, lalu dibandingkan dengan original.
        Lebih pythonic tapi kurang educational untuk otomata.
    """
    return input_string == input_string[::-1]

def display_menu():
    """
    Fungsi untuk menampilkan menu program
    
    Penjelasan:
        Menyediakan interface yang user-friendly dengan pilihan
        untuk menggunakan mode visualisasi atau mode sederhana
    """
    print("\n" + "="*50)
    print("    PALINDROME CHECKER - PRAKTIKUM OTOMATA")
    print("="*50)
    print("Pilihan:")
    print("1. Cek palindrome dengan visualisasi")
    print("2. Cek palindrome sederhana")
    print("3. Keluar")
    print("-" * 50)

def get_statistics(results):
    """
    Fungsi untuk menampilkan statistik hasil testing
    
    Args:
        results (list): List berisi hasil-hasil pengecekan
        
    Penjelasan:
        Memberikan ringkasan statistik dari session testing
        untuk analisis lebih lanjut
    """
    if not results:
        return
    
    total = len(results)
    palindrome_count = sum(1 for result in results if result['is_palindrome'])
    non_palindrome_count = total - palindrome_count
    
    print(f"\n📊 STATISTIK SESSION:")
    print(f"Total string ditest: {total}")
    print(f"Palindrome: {palindrome_count} ({palindrome_count/total*100:.1f}%)")
    print(f"Bukan palindrome: {non_palindrome_count} ({non_palindrome_count/total*100:.1f}%)")
    
    print(f"\n📝 RIWAYAT TESTING:")
    for i, result in enumerate(results, 1):
        status = "= PALINDROME" if result['is_palindrome'] else "=  BUKAN PALINDROME"
        print(f"{i:2d}. '{result['string']}' → {status}")

def main():
    """
    Fungsi utama program
    
    Penjelasan:
        Fungsi main menjalankan loop utama program dengan fitur:
        1. Menu interaktif
        2. Multiple test cases
        3. Error handling comprehensive
        4. Statistik session
        5. User experience yang baik
    """
    print("Selamat datang di Palindrome Checker!")
    print("Program untuk mengenali string palindrom dengan alphabet dan digit")
    
    # simpan hasil testing
    test_results = []
    
    while True:
        try:
            display_menu()
            choice = input("Masukkan pilihan (1-3): ").strip()
            
            if choice == '3':
                print("\n👋 Selesai!")
                get_statistics(test_results)
                break
            
            elif choice in ['1', '2']:
                input_string = input("\nMasukkan string (huruf + angka): ").strip()
                is_valid, message = validate_input(input_string)
                if not is_valid:
                    print(f"-> ERROR: {message}")
                    continue
    
                if choice == '1':
                    result = is_palindrome_with_visualization(input_string)
                else:
                    result = is_palindrome_simple(input_string)
                    status = "PALINDROME" if result else "BUKAN PALINDROME"
                    print(f"\n🔍 Hasil: String '{input_string}' adalah {status}")
                
                test_results.append({
                    'string': input_string,
                    'is_palindrome': result,
                    'method': 'visualisasi' if choice == '1' else 'sederhana'
                })
                
                continue_choice = input("\nIngin test string lain? (y/n): ").strip().lower()
                if continue_choice not in ['y', 'yes', 'ya']:
                    print("\n👋 Terima kasih telah menggunakan Palindrome Checker!")
                    get_statistics(test_results)
                    break
            
            else:
                print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan oleh user. Sampai jumpa!")
            get_statistics(test_results)
            break
        except Exception as e:
            print(f"❌ Terjadi error: {e}")
            print("Silakan coba lagi.")

# Test cases untuk demonstrasi
def run_test_cases():
    """
    Fungsi untuk menjalankan test cases otomatis
    
    Penjelasan:
        Menyediakan test cases yang comprehensive untuk demonstrasi
        dan validasi program sesuai requirement praktikum
    """
    test_cases = [
        # Test palindrome
        ("12321", True),
        ("abcba", True),
        ("A1A", True),
        ("racecar", True),
        ("12a21", True),
        
        # Test bukan palindrome
        ("hello", False),
        ("12345", False),
        ("abcd", False),
        ("A1B", False),
        
        # Test edge cases
        ("a", True),
        ("11", True),
        ("ab", False),
    ]
    
    print("🧪 RUNNING AUTOMATED TEST CASES:")
    print("-" * 40)
    
    passed = 0
    for test_string, expected in test_cases:
        result = is_palindrome_simple(test_string)
        status = " -> PASS" if result == expected else "-> FAIL"
        print(f"'{test_string}' → {result} (expected: {expected}) {status}")
        if result == expected:
            passed += 1
    
    print(f"\nTest Results: {passed}/{len(test_cases)} passed")

if __name__ == "__main__":
    # uncomment untuk menjalankan test cases otomatis
    # run_test_cases()
    main()