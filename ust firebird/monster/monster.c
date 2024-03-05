#include "stdint.h"
#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
struct attributes_t {
  uint64_t atk;
  int hp;
  char *name;
};

struct key_variables_t {
  void *enemy_actions[8];
  struct attributes_t player_att;
  struct attributes_t enemy_att;
};

void flag() {
  puts(getenv("flag"));
  exit(0);
}

void attack(struct attributes_t *a, struct attributes_t *b, int *action) {
  printf("%s uses attack!\n", a->name);
  b->hp -= a->atk;
}

void taunt(struct attributes_t *a, struct attributes_t *b, int *action) {
  printf("%s uses taunt!\n", a->name);
  printf("%s's attack doubled but forgot what it want to do next!\n", b->name);
  *action = 0;
  b->atk *= 2;
}

void gear_up(struct attributes_t *a, struct attributes_t *b, int *action) {
  printf("%s uses gear up!\n", a->name);
  a->atk += 1;
}
void rage(struct attributes_t *a, struct attributes_t *b, int *action) {
  printf("%s uses rage!\n", a->name);
  a->atk *= 2;
}
void splash(struct attributes_t *a, struct attributes_t *b, int *action) {
  printf("%s uses splash!\n", a->name);
  puts("But nothing happened.");
}
typedef void (*action_func_type)(struct attributes_t *a, struct attributes_t *b,
                                 int *action);
int main() {
  setvbuf(stdin, NULL, 2, 0);
  setvbuf(stdout, NULL, 2, 0);
  setvbuf(stderr, NULL, 2, 0);
  alarm(300);
  // I am too smart that I can use method to store the actions :)
  // Stupid Compiler, it keeps warning me :<
  struct key_variables_t key_variables = {
      .enemy_actions =
          {
              (void *)&main - (void *)&splash,
              (void *)&main - (void *)&splash,
              (void *)&main - (void *)&splash,
              (void *)&main - (void *)&splash,
              (void *)&main - (void *)&splash,
              (void *)&main - (void *)&splash,
              (void *)&main - (void *)&splash,
              (void *)&main - (void *)&attack,
          },
      .player_att = {.atk = 1, .hp = 10, .name = "player"},
      .enemy_att = {.atk = 100, .hp = 100, .name = "enemy"}};
  uint64_t action_id = 0;
  puts("Welcome to Monster!");
  while (1) {
    puts("----------------------------------------------------------");
    printf("Player attributes:\n HP: %u\nATK: %u\n",
           key_variables.player_att.hp, key_variables.player_att.atk);
    printf("Enemy attributes:\n HP: %u\nATK: %u\n", key_variables.enemy_att.hp,
           key_variables.enemy_att.atk);
    puts("Actions:");
    puts("1 Attack");
    puts("2 Taunt");
    puts("3 Gear up");
    puts("4 Rage");
    puts("5 Splash");
    puts("Choose your action: ");
    int input = 1;
    scanf("%d", &input);
    switch (input) {
    case 1:
      attack(&key_variables.player_att, &key_variables.enemy_att, &action_id);
      break;
    case 2:
      taunt(&key_variables.player_att, &key_variables.enemy_att, &action_id);
      break;
    case 3:
      gear_up(&key_variables.player_att, &key_variables.enemy_att, &action_id);
      break;
    case 4:
      rage(&key_variables.player_att, &key_variables.enemy_att, &action_id);
      break;
    case 5:
      splash(&key_variables.player_att, &key_variables.enemy_att, &action_id);
      break;
    default:
      puts("unknown input, assume you do attack");
      attack(&key_variables.player_att, &key_variables.enemy_att, &action_id);
    }
    action_func_type enemy_action =
        (void *)&main - key_variables.enemy_actions[action_id];
    enemy_action(&key_variables.enemy_att, &key_variables.player_att,
                 &action_id);
    if (key_variables.enemy_att.hp <= 0) {
      // COMP 2633 is going to start. I don't have enough time to complete it :(
      // Let's make the monster unbeatable, how smart I am. :D
      puts("How can you win? Flag is not prepared!");
      exit(0);
    }
    if (key_variables.player_att.hp <= 0) {
      puts("You died! Try Harder :D");
      exit(0);
    }
    ++action_id;
  }
}