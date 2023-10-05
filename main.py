def main():
    from game import play_game

    while True:
        play_game()
        if input("Do you want to Play again? y/n: ").lower().startswith('n'):
            break


if __name__ == '__main__':
    main()
