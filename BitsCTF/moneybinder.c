#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

uint32_t generate_key(uint32_t);
char *generate_hashtag(uint32_t, uint32_t, uint32_t, uint32_t);

int main()
{
    uint32_t initial_seed = 0;
    uint32_t key = generate_key(initial_seed);
    uint32_t year = 2024;
    for (uint32_t month = 2; month < 5; month++)
    {
        for (uint32_t day = 1; day < 32; day++)
        {
            char *hashtag = generate_hashtag(key, day, month, year);
            printf("%" PRIu32 "/%" PRIu32 "/2024: #%s\n", day, month, hashtag);
            free(hashtag);
        }
    }
    return 0;
}

char *generate_hashtag(uint32_t key, uint32_t day, uint32_t month, uint32_t year)
{
    /* Generating new_key */
    uint32_t new_key = (((key * 0x10624DD3) >> 6) * 0xFFFFFC18) + key;

    /* Current day */
    uint32_t day_key = (day << 0x10) ^ day;
    if (day_key <= 1)
    {
        day_key = day << 0x18;
    }

    /* Current month */
    uint32_t month_key = (month << 0x10) ^ month;
    if (month_key <= 7)
    {
        month_key = month << 0x18;
        if (month_key <= 7)
        {
            month_key = ~month_key;
        }
    }

    /* Current year */
    uint32_t year_key = ((year + new_key) << 0x10) ^ (year + new_key);
    if (year_key <= 0xF)
    {
        year_key = ((year + new_key) << 0x18);
    }

    /* String length */
    uint32_t string_length = (((day_key ^ ((year_key ^ 8 * year_key ^ ((day_key ^ ((month_key ^ 4 * month_key) >> 6)) >> 8)) >> 5)) >> 6) & 3) + 0xC;

    /* Generating the name */
    uint32_t index = 0;
    char *servername = calloc(string_length + 1, sizeof(char));
    servername[string_length] = '\x00';
    do
    {
        day_key = (day_key >> 0x13) ^ ((day_key >> 6) ^ (day_key << 0xC)) & 0x1FFF ^ (day_key << 0xC);
        month_key = ((month_key ^ 4 * month_key) >> 0x19) ^ 0x10 * (month_key & 0xFFFFFFF8);
        year_key = ((year_key ^ 8 * year_key) >> 0xB) ^ ((year_key & 0xFFFFFFF0) << 0x11);
        index++;
        servername[index - 1] = (day_key ^ month_key ^ year_key) % 0x19 + 'a';
    } while (index < string_length);

    return servername;
}

uint32_t generate_key(uint32_t seed)
{
    /* Stage 2: Generating the array of seeds */
    uint32_t seed_array[624];
    seed_array[0] = seed;
    for (int i = 1; i < 624; i++)
    {
        uint32_t previous_seed = seed_array[i - 1];
        uint32_t current_seed = (((previous_seed >> 0x1E) ^ previous_seed) * 0x6c078964) + i;
        seed_array[i] = current_seed;
    }

    /* Stage 3: Processing the array of seeds */
    int i = 0;
    while (i < 0xE3)
    {
        uint32_t seed_a = seed_array[i];
        uint32_t seed_b = seed_array[i + 1];
        uint32_t temp_a = (seed_a ^ seed_b) & 0x7FFFFFFF;
        i++;
        temp_a = (temp_a ^ seed_a) & 1;
        uint32_t consta[] = {0, 0x9908B0DF};
        temp_a = ((temp_a >> 1) ^ consta[0 + (temp_a & 1)]) ^ seed_array[0x18C + i];

        seed_array[i - 1] = temp_a;
    }

    /* Stage 4: Computing the DWORD value */
    uint32_t temp_b = seed_array[1];
    temp_b = ((((temp_b >> 0xB) ^ temp_b) & 0xFF3A58AD) << 0x7) ^ (temp_b >> 0xB) ^ temp_b;
    uint32_t temp_c = ((temp_b & 0xFFFFDF8C) << 0xF) ^ temp_b;
    uint32_t key = temp_c ^ (temp_c >> 0x12);

    return key;
}
