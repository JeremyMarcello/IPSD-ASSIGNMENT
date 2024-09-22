{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNJZ0EfGrCY1PjRNDSb9Vri"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yXc-mVgutAgx",
        "outputId": "f8e320fd-96df-415e-c84e-7daa0a54e1ee"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 1, 0]\n"
          ]
        }
      ],
      "source": [
        "\n",
        "p=[1,1,0,0]\n",
        "q=[1,0,1,0]\n",
        "\n",
        "def aL(p,q):\n",
        "  b=[]\n",
        "  x=0\n",
        "  for i in range(4):\n",
        "    if p[x] and q[x]:\n",
        "      b.append(1)\n",
        "    else:\n",
        "      b.append(0)\n",
        "    x+=1\n",
        "  return b\n",
        "\n",
        "def bL(p,q):\n",
        "  b=[]\n",
        "  x=0\n",
        "  for i in range(4):\n",
        "    if p[x] ^ q[x]:\n",
        "      b.append(1)\n",
        "    else:\n",
        "      b.append(0)\n",
        "    x+=1\n",
        "  return b\n",
        "\n",
        "def cL(a,b):\n",
        "  c=[]\n",
        "  x=0\n",
        "  for i in range(4):\n",
        "    if a[x] and b[x]:\n",
        "      a.append(1)\n",
        "    else:\n",
        "      a.append(0)\n",
        "    x+=1\n",
        "  return c\n",
        "\n",
        "a=aL(p,q)\n",
        "b=bL(p,q)\n",
        "c=cL(a,b)\n",
        "\n",
        "print(b)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "c1=1\n",
        "c2=1\n",
        "c3=0\n",
        "c4=0\n",
        "L=[c1,c2,c3,c4]\n",
        "print(L)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HzVtxS-vn0a8",
        "outputId": "1816f250-0218-4b0f-ff61-6eafaccaae94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 1, 0, 0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prima = []\n",
        "\n",
        "def cekPrima(n):\n",
        "    if n <= 1:\n",
        "        return False\n",
        "    for i in range(2, int(n**0.5) + 1):\n",
        "        if n % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "def barisPrima(n):\n",
        "    global prima\n",
        "    angka = 1\n",
        "    for i in range(1, n+1):\n",
        "        while len(prima) < sum(range(1,i+1)):\n",
        "            if cekPrima(angka):\n",
        "                prima.append(angka)\n",
        "            angka += 1\n",
        "        print(*prima[-i:])\n",
        "\n",
        "barisPrima(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qd9m24dx9u3i",
        "outputId": "d8747ff0-6d79-429a-eeac-6a442d7e3e03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "3 5\n",
            "7 11 13\n",
            "17 19 23 29\n",
            "31 37 41 43 47\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def cekPrima(n):\n",
        "    if n <= 1:\n",
        "        return False\n",
        "    for i in range(2, int(n**0.5) + 1):\n",
        "        if n % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "def cariPrima(x):\n",
        "    prima = []\n",
        "    for num in range(1, x + 1):\n",
        "        if cekPrima(num):\n",
        "            prima.append(num)\n",
        "    return cetakPrima(prima)\n",
        "\n",
        "# def cetakPrima(y):\n",
        "#   for i in range(rows):\n",
        "#     for j in range(i+1):\n",
        "#         print(\"* \", end=\"\")\n",
        "#   print()\n",
        "\n",
        "def cetakPrima(y):\n",
        "  n = 0\n",
        "  i = 0\n",
        "  while i < len(y):\n",
        "    for j in range(i+1):\n",
        "      print(y[n], end=\" \")\n",
        "    i += 1\n",
        "    print(\"\")\n",
        "\n",
        "\n",
        "cariPrima(40)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 408
        },
        "id": "7zXHhGDwtqCL",
        "outputId": "4cb91ec8-458b-4f5c-fe05-f61f63f3e512"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 \n",
            "3 5 \n",
            "7 11 13 \n",
            "17 19 23 29 \n",
            "31 37 "
          ]
        },
        {
          "output_type": "error",
          "ename": "IndexError",
          "evalue": "list index out of range",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-6-bb02539b40a4>\u001b[0m in \u001b[0;36m<cell line: 34>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     32\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     33\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 34\u001b[0;31m \u001b[0mcariPrima\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m40\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-6-bb02539b40a4>\u001b[0m in \u001b[0;36mcariPrima\u001b[0;34m(x)\u001b[0m\n\u001b[1;32m     12\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mcekPrima\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnum\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m             \u001b[0mprima\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnum\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mcetakPrima\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprima\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;31m# def cetakPrima(y):\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-6-bb02539b40a4>\u001b[0m in \u001b[0;36mcetakPrima\u001b[0;34m(y)\u001b[0m\n\u001b[1;32m     26\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mj\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m       \u001b[0;32mif\u001b[0m \u001b[0mn\u001b[0m \u001b[0;34m<=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 28\u001b[0;31m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\" \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     29\u001b[0m         \u001b[0mn\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     30\u001b[0m     \u001b[0mi\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mIndexError\u001b[0m: list index out of range"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# No 2 done\n",
        "def gabungList(x, y):\n",
        "  list1 = []\n",
        "  list2 = []\n",
        "  index = 1\n",
        "  for i in range(len(x)):\n",
        "    if i%2 == 1:\n",
        "      list1.append(x[i])\n",
        "  for i in range(len(y)):\n",
        "    if i%2 == 1:\n",
        "      list2.append(y[i])\n",
        "  list3 = list1+list2\n",
        "  list3.sort(reverse=True)\n",
        "  return list3\n",
        "\n",
        "gabungList([3,1,2,5],[6,4,8,7])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VQw-pWP0wRy7",
        "outputId": "98d9a050-0e43-4ea4-dda5-7d108b4e681b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[7, 5, 4, 1]"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def tebakAngka():\n",
        "    angka = random.randint(1, 100)\n",
        "    batasPercobaan = 5\n",
        "    percobaan = 0\n",
        "    batasBawah = 1\n",
        "    batasAtas = 100\n",
        "    print(\"Selamat datang di permainan tebak angka!\")\n",
        "    print(\"Komputer telah memilih sebuah angka antara 1 hingga 100.\")\n",
        "    print(f\"Anda memiliki {batasPercobaan} kesempatan untuk menebaknya.\")\n",
        "    while percobaan < batasPercobaan:\n",
        "        try:\n",
        "            tebakan = int(input(f\"Tebakan ke-{percobaan + 1}: Masukkan angka Anda (antara {batasBawah} dan {batasAtas}): \"))\n",
        "            if tebakan < batasBawah or tebakan > batasAtas:\n",
        "                print(f\"Angka di luar batas! Silakan masukkan angka antara {batasBawah} dan {batasAtas}.\")\n",
        "                continue\n",
        "            percobaan += 1\n",
        "            if tebakan == angka:\n",
        "                print(f\"Selamat! Anda berhasil menebak angka {angka} dengan benar.\")\n",
        "                return\n",
        "            elif tebakan < angka:\n",
        "                print(\"Tebakan Anda terlalu kecil.\")\n",
        "                batasBawah = tebakan + 1\n",
        "            else:\n",
        "                print(\"Tebakan Anda terlalu besar.\")\n",
        "                batasAtas = tebakan - 1\n",
        "            print(f\"Petunjuk: Coba angka antara {batasBawah} dan {batasAtas}.\")\n",
        "        except ValueError:\n",
        "            print(\"Input tidak valid. Silakan masukkan angka.\")\n",
        "    print(f\"Anda kehabisan kesempatan. Angka yang benar adalah {angka}.\")\n",
        "    print(\"Permainan selesai. Semoga beruntung lain kali!\")\n",
        "\n",
        "tebakAngka()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PDH6_JK1EMSv",
        "outputId": "d6109efb-897a-4f52-9040-09b37fd3c2c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Selamat datang di permainan tebak angka!\n",
            "Komputer telah memilih sebuah angka antara 1 hingga 100.\n",
            "Anda memiliki 5 kesempatan untuk menebaknya.\n",
            "Tebakan ke-1: Masukkan angka Anda (antara 1 dan 100): 50\n",
            "Tebakan Anda terlalu besar.\n",
            "Petunjuk: Coba angka antara 1 dan 49.\n",
            "Tebakan ke-2: Masukkan angka Anda (antara 1 dan 49): 30\n",
            "Tebakan Anda terlalu besar.\n",
            "Petunjuk: Coba angka antara 1 dan 29.\n",
            "Tebakan ke-3: Masukkan angka Anda (antara 1 dan 29): 20\n",
            "Tebakan Anda terlalu besar.\n",
            "Petunjuk: Coba angka antara 1 dan 19.\n",
            "Tebakan ke-4: Masukkan angka Anda (antara 1 dan 19): 10\n",
            "Tebakan Anda terlalu kecil.\n",
            "Petunjuk: Coba angka antara 11 dan 19.\n",
            "Tebakan ke-5: Masukkan angka Anda (antara 11 dan 19): 16\n",
            "Tebakan Anda terlalu besar.\n",
            "Petunjuk: Coba angka antara 11 dan 15.\n",
            "Anda kehabisan kesempatan. Angka yang benar adalah 11.\n",
            "Permainan selesai. Semoga beruntung lain kali!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g3rT13xizVut",
        "outputId": "89b1fe5c-5b63-4d92-8409-38eae76a7a14"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[7, 5, 4, 1]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "userPin = \"1234\"\n",
        "saldo = 100000\n",
        "\n",
        "def cek_pin():\n",
        "    percobaan = 0\n",
        "    while percobaan < 3:\n",
        "        try:\n",
        "            pin = input(\"Masukkan PIN Anda: \")\n",
        "            if not pin.isdigit():\n",
        "                raise ValueError(\"PIN hanya boleh berisi angka.\")\n",
        "            if pin == userPin:\n",
        "                print(\"PIN benar.\")\n",
        "                return True\n",
        "            else:\n",
        "                percobaan += 1\n",
        "                print(f\"PIN salah. Percobaan ke-{percobaan}.\")\n",
        "        except ValueError as ve:\n",
        "            print(f\"Kesalahan: {ve}\")\n",
        "    print(\"PIN salah 3 kali. Akses diblokir.\")\n",
        "    return False\n",
        "\n",
        "def tarik_saldo():\n",
        "    global saldo\n",
        "    try:\n",
        "        jumlah_tarik = int(input(\"Masukkan jumlah penarikan: \"))\n",
        "        if not jumlah_tarik.isdigit():\n",
        "            raise TypeError(\"Saldo hanya boleh berisi angka.\")\n",
        "        elif jumlah_tarik > saldo:\n",
        "            raise ValueError(\"Saldo tidak mencukupi.\")\n",
        "        saldo -= jumlah_tarik\n",
        "        print(f\"Penarikan berhasil. Saldo Anda sekarang: {saldo}\")\n",
        "    except ValueError as ve:\n",
        "        print(f\"Kesalahan: {ve}\")\n",
        "    except TypeError as te:\n",
        "        print(f\"Kesalahan: {te}\")\n",
        "\n",
        "def main():\n",
        "    if cek_pin():\n",
        "        tarik_saldo()\n",
        "\n",
        "main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0jSj-aJBlF6I",
        "outputId": "e2bc2ee7-dbe7-40aa-b3e3-58b4e5f99a5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan PIN Anda: 1234\n",
            "PIN benar.\n",
            "Masukkan jumlah penarikan: p\n",
            "Kesalahan: invalid literal for int() with base 10: 'p'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "jumlah_tarik = input(\"masukkan jumlah: \")\n",
        "saldo=100\n",
        "\n",
        "if jumlah_tarik > saldo:\n",
        "        raise ValueError(\"Saldo tidak mencukupi.\")\n",
        "        saldo -= jumlah_tarik\n",
        "        print(f\"Penarikan berhasil. Saldo Anda sekarang: {saldo}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        },
        "id": "QpvyrbKtxuIA",
        "outputId": "ac286a46-cf06-46e5-c399-5a460ee7eedb"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "masukkan jumlah: p\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "'>' not supported between instances of 'str' and 'int'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-bb2dcff6997d>\u001b[0m in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0msaldo\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mif\u001b[0m \u001b[0mjumlah_tarik\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0msaldo\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Saldo tidak mencukupi.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m         \u001b[0msaldo\u001b[0m \u001b[0;34m-=\u001b[0m \u001b[0mjumlah_tarik\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: '>' not supported between instances of 'str' and 'int'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def minimalCoin(coins, amount):\n",
        "  coins.sort(reverse=True)\n",
        "  kombinasiCoin = []\n",
        "\n",
        "  for coin in coins:\n",
        "    if amount == 0:\n",
        "      break\n",
        "    while amount >= coin:\n",
        "      amount -= coin\n",
        "      kombinasiCoin.append(coin)\n",
        "\n",
        "  if amount == 0:\n",
        "    return kombinasiCoin\n",
        "  else:\n",
        "    return \"Tidak ada solusi dengan koin yang diberikan.\"\n",
        "\n",
        "coins = [1, 5, 10, 25]\n",
        "amount = 63\n",
        "kombinasiCoin = minimalCoin(coins, amount)\n",
        "\n",
        "print(f\"Jumlah koin minimum yang dibutuhkan: {len(kombinasiCoin)}\")\n",
        "print(f\"Koin yang digunakan: {kombinasiCoin}\")"
      ],
      "metadata": {
        "id": "MfHOvBn7v2F1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "32a1755a-8e5f-49cf-99b3-2350ae381293"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jumlah koin minimum yang dibutuhkan: 6\n",
            "Koin yang digunakan: [25, 25, 10, 1, 1, 1]\n"
          ]
        }
      ]
    }
  ]
}